from __future__ import annotations

import random

from src.settings import CONFIG


class Spawner:
    def __init__(self, obstacle_manager, collectible_manager) -> None:
        self.obstacle_manager = obstacle_manager
        self.collectible_manager = collectible_manager
        self.cooldown = CONFIG.obstacle_spawn_interval

    def update(self, dt: float, scroll_speed: float, difficulty) -> None:
        self.cooldown -= dt
        if self.cooldown <= 0:
            self.obstacle_manager.spawn(difficulty.level)
            newest = self.obstacle_manager.items[-1]

            if random.random() <= CONFIG.collectible_spawn_chance:
                cx = newest.x + newest.width / 2 - 12
                cy = newest.gap_y + newest.gap_height / 2 - 12
                self.collectible_manager.spawn(cx, cy)

            self.cooldown = difficulty.current_spawn_interval(CONFIG.obstacle_spawn_interval)
