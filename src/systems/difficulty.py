from __future__ import annotations

from src.settings import CONFIG


class DifficultyController:
    def __init__(self) -> None:
        self.elapsed = 0.0
        self.level = 1

    def update_level(self, dt: float) -> None:
        self.elapsed += dt
        self.level = 1 + int(self.elapsed // 12)

    def current_speed(self, base_speed: float) -> float:
        if not CONFIG.difficulty_scaling:
            return base_speed
        return base_speed + (self.level - 1) * 20.0

    def current_spawn_interval(self, base_interval: float) -> float:
        if not CONFIG.difficulty_scaling:
            return base_interval
        interval = base_interval - (self.level - 1) * 0.06
        return max(0.85, interval)
