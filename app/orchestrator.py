from clarification_agent import clarify_requirements
from planning_agent import create_plan
from codegen_agent import generate_code
from file_writer import write_game_files


def run():
    print("🎮 Agentic Game Builder AI\n")

    print("Describe your game idea first:")
    input("> ")

    # ---- Phase 1: Clarification ----
    requirements = clarify_requirements()

    print("\n✅ Finalized Requirements:")
    print(requirements.model_dump_json(indent=2))

    # ---- Phase 2: Planning ----
    plan = None
    while plan is None:
        plan = create_plan(requirements)

    print("\n🧠 Generated Technical Plan:")
    print(plan.model_dump_json(indent=2))

    # ---- Phase 3: Code Generation ----
    code = None
    while code is None:
        code = generate_code(requirements, plan)

    # ---- Write Files ----
    write_game_files(code)

    print("\n🎉 Game generation complete!")
    print("Open generated_games/index.html in your browser.")


if __name__ == "__main__":
    run()
