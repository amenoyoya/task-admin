# task-admin


タスク管理アプリ

## Environment

- Docker: `19.03.2`
- DockerCompose: `1.24.0`
- CLI:
    - Node.js: `10.15.3`
    - yarn: `1.15.2`

### Structure
```bash
./
 |_ app/  # Webアプリケーション本体
 |   |_ seerver/
 |   |   |_ static/ # 静的ファイル配置
 |   |   |   |_ js/
 |   |   |       |_ bundle.js # webpackバンドル後のJSファイル
 |   |   |
 |   |   |_ __init__.py   # ライブラリ本体
 |   |   |_ auth_api.py   # ユーザー認証API
 |   |   |_ config.yml    # 設定ファイル
 |   |   |_ server.py     # Flaskサーバー
 |   |
 |   |_ src/
 |   |   |_ index.js      # Vueソースコード（エントリーポイント）
 |   |
 |   |_ vassals/
 |   |   |_ server.ini    # FlaskサーバーのuWSGI設定
 |   |
 |   |_ package.json      # Node.js依存モジュール定義
 |   |_ webpack.config.js # webpackバンドル設定
 |
 |_ flask/ # flaskコンテナ
 |   |_ Dockerfile        # ビルド設定
 |   |_ requirements.txt  # Python依存モジュール定義
 |
 |_ web/   # webコンテナ
 |   |_ Dockerfile        # ビルド設定
 |   |_ nginx.conf        # nginx設定ファイル
 |
 |_ docker-compose.yml    # DockerComposeビルド設定
                          # - web:   Nginx 1.17 | http://task-admin.localhost
                          # - flask: Python 3.7 + Flask + uWSGI
```

### Setup
```bash
# 設定ファイル作成
$ cp app/server/config.yml.default app/server/config.yml

# Dockerコンテナをビルド＆起動
$ docker-compose build
$ docker-compose up -d

# appディレクトリに移動
$ cd app

# node.js 開発開始
$ yarn install # 依存パッケージインストール
$ yarn watch   # js, vue ファイル変更検知＆バンドル
```

***

## Spec

### Log
- nginxログ:
    ```bash
    # attach web container
    $ docker-compose exec web bash
    ---
    % cd /etc/nginx/logs/
    # access.log, error.log
    % less access.log
    % less error.log
    ```
- uWSGIログ:
    ```bash
    # attach flask container
    $ docker-compose exec flask ash
    ---
    % cd /var/log/
    # server.log
    % less server.log
    ```

***

## Eel版

### What's this?
- Eel:
    - Local GUI application libarary for python by Chrome Browser

### Environment
- OS:
    - Windows 10
    - Ubuntu 18.04
- Applications:
    - Python: `3.7`
    - Google Chrome Browser

### Setup
```bash
# project dir: _eel
$ cd ./_eel/

# install python modules
$ pip install -r requirements.txt

# start eel application
$ python main.py
```

***

## Electron版

### What's this?
- Electron:
    - Local GUI application libarary for Node.js

### Environment
- OS:
    - Windows 10
    - Ubuntu 18.04
- Applications:
    - Node.js: `10.15.3`
        - yarn package manager: `1.15.2`

### Setup
```bash
# project dir: _electron
$ cd ./_electron/

# install node modules
$ yarn install

# global install: electron
$ yarn global add electron-prebuilt

# PATHが通っていないなら通しておく
## `yarn global bin` で表示されるPATHを通す

# start electron application
$ electron main.js
```
