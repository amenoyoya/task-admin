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

# POST /api/get/todo/
## todoリスト取得
@Application.cmd('/api/get/todo/', methods=['POST'])
def get_todo_api():
    with open('./static/data.json') as f:
        return jsonify(json.load(f))

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
