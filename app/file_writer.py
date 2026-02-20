import os
from schemas import GeneratedCode


OUTPUT_DIR = "generated_games"


def write_game_files(code: GeneratedCode):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(os.path.join(OUTPUT_DIR, "index.html"), "w") as f:
        f.write(code.index_html)

    with open(os.path.join(OUTPUT_DIR, "style.css"), "w") as f:
        f.write(code.style_css)

    with open(os.path.join(OUTPUT_DIR, "game.js"), "w") as f:
        f.write(code.game_js)

    print(f"\n✅ Game files written to ./{OUTPUT_DIR}/")
