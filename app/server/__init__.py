from flask import Flask, Response, request, session, redirect, jsonify
from functools import wraps
import yaml, secrets

# Flaskアプリケーション・ラッパークラス
class Application(object):
    flask = None
    config = {}

    # Flaskアプリケーション作成
    @staticmethod
    def create(import_name: str, **options):
        Application.flask = Flask(import_name, **options)
        Application.flask.secret_key = secrets.token_hex() # セッション暗号化

        # load configurations
        with open('./config.yml') as f:
            Application.config = yaml.load(f)

        # / => config.server.root_html 表示
        @Application.flask.route('/')
        def index():
            csrf = session.get('csrf')
            if csrf is None:
                csrf = secrets.token_hex()
                session['csrf'] = csrf # CSRFトークンをセッション保存
            return Application.config['server']['root_html'].format(csrf=csrf)

        # POST /api/ => APIサーバー設定を返す
        @Application.cmd('/api/', methods=['POST'])
        def api():
            return jsonify({
                'endpoints': Application.config['endpoints']
            })


        # 404 not found => redirect to root url ?redirect=<request.path>
        @Application.flask.errorhandler(404)
        def error_handler(error):
            return redirect('/?redirect=' + request.path)
        
        return Application.flask

    # サーバー実行
    @staticmethod
    def run(**options):
        Application.flask.run(**options)

    # ルーティング定義デコレータ
    @staticmethod
    def route(rule: str, **options):
        return Application.flask.route(rule, **options)
    
    # クライアントIPアドレス取得
    @staticmethod
    def get_client_ip():
        if 'HTTP_X_FORWARDED_FOR' in request.environ:
            return request.environ['HTTP_X_FORWARDED_FOR']
        if 'HTTP_X_REAL_IP' in request.environ:
            return request.environ['HTTP_X_REAL_IP']
        return request.environ.get('REMOTE_ADDR')
    
    # CORS対応Response生成
    @staticmethod
    def generate_cors_response(resp=None):
        # 全てのリクエスト元, リクエストメソッド, リクエストヘッダー, レスポンスヘッダーを許可
        return Response(resp, headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Expose-Headers': '*'
        })

    # 外部実行用API定義デコレータ: 誰でも or 許可されたIP から実行可能
    @staticmethod
    def api(rule: str, **options):
        def _wrapper(func):
            @wraps(func) # デコレートした関数名が`wrapper`になるのを防ぐ: ルーティングを複数定義したとき関数名が上書きされるのを防ぐ
            def wrapper(*args, **kargs):
                # check ips
                if not Application._check_ips():
                    res = Application.generate_cors_response('')
                    res.status_code = 403 # Forbidden error
                    return res
                # return CORS対応response
                return Application.generate_cors_response(func(*args, **kargs))
            return Application.route(rule, **options)(wrapper)
        return _wrapper
        
    # 内部実行用API定義デコレータ: CSRFトークンとホスト名のチェックを行う
    ## フロントエンドJavaScriptからAjax通信で実行する場合などに使う
    @staticmethod
    def cmd(rule: str, **options):
        def _wrapper(func):
            @wraps(func) # デコレートした関数名が`wrapper`になるのを防ぐ: ルーティングを複数定義したとき関数名が上書きされるのを防ぐ
            def wrapper(*args, **kargs):
                csrf = request.json['csrf'] if isinstance(request.json, dict) and 'csrf' in request.json else (
                    request.form['csrf'] if isinstance(request.form, dict) and 'csrf' in request.form else ''
                )
                # check csrf token & host name
                if not Application._check_csrf(csrf) or request.host != Application.config['server']['host']:
                    return '', 403 # Forbidden error
                return func(*args, **kargs)
            return Application.route(rule, **options)(wrapper)
        return _wrapper

    # @private API IP制限: config.yml/api.ips の設定に従ってチェックする
    ## @return bool true => 許可されているIP or 制限なし, false => 許可されていないIP
    @staticmethod
    def _check_ips():
        if isinstance(Application.config['api']['accept_ips'], list):
            if Application.get_client_ip() in Application.config['api']['accept_ips']:
                return True
            return False
        return Application.config['api']['accept_ips']

    # @private API CSRFチェック
    ## @return bool true => CSRF一致, false => CSRF不一致
    @staticmethod
    def _check_csrf(csrf: str):
        return 'csrf' in session and session['csrf'] == csrf
