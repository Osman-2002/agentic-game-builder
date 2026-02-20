import json
from schemas import GameRequirements
from llm import call_llm


REQUIRED_FIELDS = [
    "genre",
    "player_goal",
    "controls",
    "win_condition",
    "lose_condition",
    "difficulty",
    "target_platform"
]


EXTRACTION_PROMPT = """
You are a smart information extractor.

From the user's natural language input, extract any relevant information
about the following fields if present:

- genre (e.g., action, strategy, arcade)
- player_goal (what the player is trying to achieve)
- controls (keyboard, mouse, touch — return as list)
- win_condition
- lose_condition
- difficulty (easy, medium, hard)
- target_platform (desktop or mobile)

IMPORTANT RULES:
- The user may NOT use structured phrases.
- Infer meaning naturally.
- If they say "PC", convert to "desktop".
- If they say "clicking cells", infer controls as ["mouse"].
- If they say "three in a row", infer win_condition properly.
- Controls MUST be returned as a list.
- Return ONLY valid JSON.
- If nothing is found, return {}.

Example input:
"It’s a tic tac toe game where you click cells to get three in a row."

Example output:
{
  "genre": "strategy",
  "controls": ["mouse"],
  "win_condition": "form three in a row"
}
"""




def extract_fields(user_input: str):
    output = call_llm(EXTRACTION_PROMPT, user_input)

    try:
        return json.loads(output)
    except Exception:
        return {}


def clarify_requirements():
    collected_data = {}

    print("\nLet’s design your game together.")
    print("You can describe it naturally — no strict format needed.\n")

    while True:
        missing = [f for f in REQUIRED_FIELDS if f not in collected_data]

        if not missing:
            try:
                validated = GameRequirements(**collected_data)
                return validated
            except Exception as e:
                print("Validation error:", e)
                collected_data = {}

        print("\nTell me more about the game.")
        print("You can answer naturally in one or multiple sentences.")
        print("Example:")
        print('"It’s a strategy game for desktop where players click cells to form three in a row."')
        print("\nDetails still missing:")
        for field in missing:
            print(f"- {field}")

        user_input = input("\nYour answer: ")

        extracted = extract_fields(user_input)

        for key, value in extracted.items():
            if key == "controls" and isinstance(value, str):
                collected_data[key] = [value]
            else:
                collected_data[key] = value

