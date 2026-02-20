import json
from schemas import GamePlan, GameRequirements
from llm import call_llm


SYSTEM_PROMPT = """
You are a game architecture planning agent.

Design a simple implementation plan for a small playable browser game.

STRICT RULES:

- Use vanilla JavaScript
- Use HTML5 Canvas
- Use requestAnimationFrame
- Keep everything simple

CRITICAL:
- "entities" MUST be a list of strings.
- "systems" MUST be a list of strings.
- DO NOT return objects inside entities or systems.
- DO NOT nest JSON inside entities or systems.

Return ONLY valid JSON in EXACTLY this structure:

{
  "engine": "vanilla-js",
  "rendering_strategy": "short description",
  "game_loop": "short description",
  "state_management": ["state1", "state2"],
  "entities": ["Player", "Enemy", "Bullet"],
  "systems": ["InputSystem", "CollisionSystem", "ScoreSystem"]
}
"""



def create_plan(requirements: GameRequirements):
    user_prompt = f"""
Game Requirements:
{requirements.model_dump_json(indent=2)}

Design the internal architecture and implementation plan.
Return JSON only.
"""

    output = call_llm(SYSTEM_PROMPT, user_prompt)

    try:
        data = json.loads(output)
        validated = GamePlan(**data)
        return validated
    except Exception:
        print("\n❌ Planning phase failed. Raw LLM output:")
        print(output)
        return None
