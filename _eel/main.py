import os, sys, json, eel
from markdown import markdown

# --- Eel公開関数 ---
## システム終了: None -> None
@eel.expose
def exit_system() -> None:
    sys.exit()

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
## start: ./assets/main.html
eel.init('assets')
eel.start('main.html')
