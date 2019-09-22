import os, sys, eel

# --- Eel公開関数 ---
## システム終了: None -> None
@eel.expose
def exit_system() -> None:
    sys.exit()

eel.init('assets')
eel.start('main.html')
