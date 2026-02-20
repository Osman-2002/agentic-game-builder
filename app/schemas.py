from pydantic import BaseModel
from typing import List, Literal


class GameRequirements(BaseModel):
    genre: str
    player_goal: str
    controls: List[str]
    win_condition: str
    lose_condition: str
    difficulty: str
    target_platform: Literal["desktop", "mobile"]


class GamePlan(BaseModel):
    engine: Literal["vanilla-js"]
    rendering_strategy: str
    game_loop: str
    state_management: List[str]
    entities: List[str]
    systems: List[str]


class GeneratedCode(BaseModel):
    index_html: str
    style_css: str
    game_js: str
