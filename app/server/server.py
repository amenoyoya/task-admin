from __init__ import Application
import os

app = Application.create(__name__)
import auth_api

# GET /api/markdown/<filename> => <filename>のMarkdownをHTMLに変換して返す
@Application.api('/markdown/<string:filename>', methods=['GET'])
def md(filename):
    path = f'./markdown/{filename}.md'
    if not os.path.isfile(path):
        return 'file not found'
    with open(path) as f:
        return markdown(f.read(), extensions=[
            'extra', 'admonition', 'codehilite', 'meta', 'nl2br', 'sane_lists', 'smarty', 'wikilinks'
        ])

if __name__ == '__main__':
    Application.run(debug=True)
