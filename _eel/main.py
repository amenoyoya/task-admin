import bottle_websocket, eel
import os, sys, json, yaml
from markdown import markdown

# --- Eel公開関数 ---
## convert markdown code to html: str -> str
@eel.expose
def convert_markdown(md: str) -> str:
    return markdown(md, extensions=[
        'extra', 'admonition', 'codehilite', 'meta', 'nl2br', 'sane_lists', 'smarty', 'wikilinks'
    ])

## taskリスト取得: None -> list{list{dict, 1}, 1}
@eel.expose
def load_tasks() -> list:
    if not os.path.isfile('./tasks.json'):
        return [[], [], [], []]
    with open('./tasks.json') as f:
        return json.load(f)

## tasksリスト更新: list{list{dict, 1}, 1} -> None
@eel.expose
def save_tasks(tasks: list) -> None:
    with open('./tasks.json', 'w') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

# --- Eel Application ---
## load config.yml
options = {'eel': {}}
if os.path.isfile('./config.yml'):
    with open('./config.yml') as f:
        options = yaml.load(f)

## start: ./assets/main.html
## close callback: システム終了
eel.init('assets')
eel.start('main.html', close_callback = lambda: sys.exit(), **options['eel'])
