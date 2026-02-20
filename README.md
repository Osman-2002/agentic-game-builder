**🎮 Agentic Game Builder AI
**Overview

This project implements a multi-phase Agentic AI system capable of:

Accepting ambiguous natural-language game ideas

Asking clarification questions

Designing a structured internal plan

Generating a fully playable HTML/CSS/JavaScript game

Outputting runnable files locally

Running entirely inside a Docker container

The system is designed with clear control flow, structured validation, and deterministic agent orchestration.

🧠 Agent Architecture

The system is built as a modular multi-agent pipeline:

User Input
   ↓
Clarification Agent
   ↓
Planning Agent
   ↓
Code Generation Agent
   ↓
File Writer
   ↓
Playable Game Output
1️⃣ Clarification Agent

Extracts structured game requirements from natural language.

Identifies missing fields.

Uses schema validation to ensure completeness.

Accepts flexible, conversational input.

Outputs structured requirements:

{
  "genre": "...",
  "player_goal": "...",
  "controls": ["..."],
  "win_condition": "...",
  "lose_condition": "...",
  "difficulty": "...",
  "target_platform": "desktop | mobile"
}
2️⃣ Planning Agent

Designs internal game architecture including:

Framework decision (Vanilla JS)

Rendering strategy (HTML5 Canvas)

Game loop (requestAnimationFrame)

State management

Core systems

Game entities

Outputs a structured architecture plan before any code is generated.

3️⃣ Code Generation Agent

Generates:

index.html

style.css

game.js

Constraints:

Vanilla JavaScript only

No external libraries

No CDN dependencies

Fully offline runnable

Opens directly in browser

4️⃣ File Writer

Writes generated files to:

generated_games/
 ├── index.html
 ├── style.css
 └── game.js

The game runs by simply opening index.html in a browser.

🏗 Technical Design Decisions
Framework Choice

Vanilla JavaScript was chosen over Phaser to:

Avoid CDN dependencies

Ensure full offline compatibility

Simplify container execution

Structured Validation

Each phase uses Pydantic schema validation to:

Prevent malformed outputs

Enforce deterministic transitions

Reduce hallucinated structure

Deterministic Orchestration

The LLM does not control state.
Python manages control flow and validation explicitly.

🐳 Running With Docker (Mandatory Requirement)
1️⃣ Build Docker Image

From project root:

docker build -t agentic-game-builder .
2️⃣ Run With OpenAI API
docker run -it \
  -e OPENAI_API_KEY=your_openai_key_here \
  -v $(pwd)/generated_games:/app/generated_games \
  agentic-game-builder
3️⃣ Run With xAI (Grok API)
docker run -it \
  -e XAI_API_KEY=your_xai_key_here \
  -e LLM_PROVIDER=xai \
  -v $(pwd)/generated_games:/app/generated_games \
  agentic-game-builder
4️⃣ Open Generated Game

After generation:

generated_games/index.html

Open it in your browser.

📦 Project Structure
agentic-game-builder/
│
├── app/
│   ├── orchestrator.py
│   ├── clarification_agent.py
│   ├── planning_agent.py
│   ├── codegen_agent.py
│   ├── file_writer.py
│   ├── schemas.py
│   └── llm.py
│
├── generated_games/
├── Dockerfile
├── requirements.txt
└── README.md
⚖️ Trade-offs

Chose Vanilla JS over Phaser for simplicity and reliability.

Single-pass code generation instead of iterative refinement.

CLI-based interaction instead of a web interface.

Strict schema enforcement improves reliability but reduces flexibility.

🚀 Improvements With More Time

Add automatic retry and structured error recovery

Add automated tests for each phase

Add support for multiple frameworks (Phaser option)

Add web-based UI instead of CLI

Improve planning depth (explicit mechanics modeling)

Add logging and observability

Add memory for multi-turn refinement

🔐 Security Notes

API keys are not stored inside the container.

Environment variables must be passed at runtime.

.env is excluded from version control.

✅ Submission Checklist

✔ Multi-phase agent architecture

✔ Requirements clarification

✔ Structured planning

✔ Playable HTML/CSS/JS output

✔ Dockerized execution

✔ Clear README documentation

✔ Deterministic control flow

✔ No hard-coded game template

🎯 Final Result

A fully containerized agentic AI system capable of designing and generating small playable games from ambiguous natural-language input.
