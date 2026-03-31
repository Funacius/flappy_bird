from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    screen_width: int = 960
    screen_height: int = 540
    ground_height: int = 50
    title: str = "Infinite Flyer"
    fps: int = 60

    gravity: float = 1400.0
    flap_impulse: float = -420.0
    base_scroll_speed: float = 240.0

    obstacle_spawn_interval: float = 1.35
    collectible_spawn_chance: float = 0.75

    player_x: int = 180
    player_start_y: int = 240
    player_width: int = 56
    player_height: int = 40

    obstacle_width: int = 90
    obstacle_gap_min: int = 140
    obstacle_gap_max: int = 190
    obstacle_margin_y: int = 70

    dynamic_obstacles: bool = True
    difficulty_scaling: bool = True
    particle_effects: bool = True

CONFIG = Config()
