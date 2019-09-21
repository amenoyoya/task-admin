from __init__ import Application, jsonify, request
from markdown import markdown
import os, json

app = Application.create(__name__)
# import auth_api

# convert markdown code to html
def convert_markdown(md: str):
    return markdown(md, extensions=[
        'extra', 'admonition', 'codehilite', 'meta', 'nl2br', 'sane_lists', 'smarty', 'wikilinks'
    ])

# POST /api/get/tasks/
## taskリスト取得
@Application.cmd('/api/get/tasks/', methods=['POST'])
def get_todo_api():
    if not os.path.isfile('./tasks.json'):
        return jsonify({
            'message': 'tasks.json not found'
        }), 500
    with open('./tasks.json') as f:
        return jsonify(json.load(f))

# POST /api/post/tasks/
## tasksリスト更新
@Application.cmd('/api/put/tasks/', methods=['POST'])
def put_todo_api():
    with open('./tasks.json', 'w') as f:
        json.dump(request.json.get('tasks'), f, ensure_ascii=False, indent=2)
        return '', 204 # No Content

# POST /api/post/markdown/
## MarkdownをHTML変換
@Application.cmd('/api/post/markdown/', methods=['POST'])
def convert_markdown_api():
    markdown = request.json['markdown'] if 'markdown' in request.json else ''
    return jsonify({
        'html': convert_markdown(markdown)
    })

if __name__ == '__main__':
    Application.run(debug=True)
