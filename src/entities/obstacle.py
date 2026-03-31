# obstacle.py (Updated for Object Pooling)
from __future__ import annotations
from dataclasses import dataclass
import math
import random
import pygame

from src.settings import CONFIG
from src.core.object_pool import ObjectPool  # <-- Import your pool


@dataclass
class ObstaclePair:
    x: float = 0.0
    gap_y: int = 0
    gap_height: int = 0
    width: int = 0
    active: bool = True
    scored: bool = False
    dynamic_offset: float = 0.0
    phase: float = 0.0

    # Add a reset method to re-initialize recycled objects
    def reset(self, x: float, gap_y: int, gap_height: int, width: int, phase: float):
        self.x = x
        self.gap_y = gap_y
        self.gap_height = gap_height
        self.width = width
        self.active = True
        self.scored = False
        self.dynamic_offset = 0.0
        self.phase = phase

    def top_rect(self) -> pygame.Rect:
        height = max(0, self.gap_y - self.dynamic_offset)
        return pygame.Rect(int(self.x), 0, self.width, int(height))

    def bottom_rect(self) -> pygame.Rect:
        y = int(self.gap_y + self.gap_height - self.dynamic_offset)
        h = CONFIG.screen_height - y
        return pygame.Rect(int(self.x), y, self.width, h)


class ObstacleManager:
    def __init__(self) -> None:
        self.items: list[ObstaclePair] = []
        # Initialize the pool with a factory function
        self.pool: ObjectPool[ObstaclePair] = ObjectPool(lambda: ObstaclePair(), initial_size=5)

    def spawn(self, difficulty_level: int = 1) -> None:
        gap_height = random.randint(CONFIG.obstacle_gap_min, CONFIG.obstacle_gap_max)
        gap_y = random.randint(CONFIG.obstacle_margin_y, CONFIG.screen_height - CONFIG.obstacle_margin_y - gap_height)

        # ACQUIRE from pool instead of creating new
        obstacle = self.pool.acquire()
        obstacle.reset(
            x=CONFIG.screen_width + 30,
            gap_y=gap_y,
            gap_height=gap_height,
            width=CONFIG.obstacle_width,
            phase=random.uniform(0.0, math.pi * 2)
        )
        self.items.append(obstacle)

    def update(self, dt: float, scroll_speed: float) -> None:
        alive_items: list[ObstaclePair] = []
        for obstacle in self.items:
            obstacle.x -= scroll_speed * dt

            if CONFIG.dynamic_obstacles:
                obstacle.phase += dt * 1.6
                obstacle.dynamic_offset = math.sin(obstacle.phase) * 18.0

            # If still on screen, keep it. Otherwise, RELEASE to pool.
            if obstacle.x + obstacle.width > 0:
                alive_items.append(obstacle)
            else:
                self.pool.release(obstacle)  # <-- Return to pool!

        self.items = alive_items

    def consume_passed(self, player_x: float) -> int:
        score = 0
        for obstacle in self.items:
            if not obstacle.scored and obstacle.x + obstacle.width < player_x:
                obstacle.scored = True
                score += 1
        return score

    def draw(self, screen: pygame.Surface) -> None:
        for obstacle in self.items:
            # For now, let's just make the green a bit nicer with a border
            # until you decide to add a rock/pipe image!
            pygame.draw.rect(screen, (70, 150, 70), obstacle.top_rect())
            pygame.draw.rect(screen, (50, 100, 50), obstacle.top_rect(), 4)  # Border

            pygame.draw.rect(screen, (70, 150, 70), obstacle.bottom_rect())
            pygame.draw.rect(screen, (50, 100, 50), obstacle.bottom_rect(), 4)  # Border
