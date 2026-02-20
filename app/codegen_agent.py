import json
from schemas import GeneratedCode, GameRequirements, GamePlan
from llm import call_llm


SYSTEM_PROMPT = """
You are a game code generation agent.

Generate a small playable browser game using:

- HTML
- CSS
- Vanilla JavaScript
- HTML5 Canvas
- requestAnimationFrame

STRICT RULES:

- The game must run locally by opening index.html in a browser.
- No external libraries.
- No CDN links.
- All logic must be in game.js.
- index.html must link style.css and game.js correctly.
- Use <canvas> element.
- Keep game simple and playable.
- Implement basic player movement.
- Implement enemies.
- Implement score tracking.
- Implement lives system.
- Implement game over state.

Return ONLY valid JSON in EXACTLY this format:

{
  "index_html": "...",
  "style_css": "...",
  "game_js": "..."
}

Do not include markdown.
Do not include explanations.
Only return valid JSON.
"""


def generate_code(requirements: GameRequirements, plan: GamePlan):
    user_prompt = f"""
Game Requirements:
{requirements.model_dump_json(indent=2)}

Technical Plan:
{plan.model_dump_json(indent=2)}

Generate complete working code files.
Return JSON only.
"""

    output = call_llm(SYSTEM_PROMPT, user_prompt)

    try:
        data = json.loads(output)
        validated = GeneratedCode(**data)
        return validated
    except Exception:
        print("\n❌ Code generation failed. Raw output:")
        print(output)
        return None
