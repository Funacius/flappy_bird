from __future__ import annotations

from dataclasses import dataclass
import math
import random
import pygame

from src.settings import CONFIG


@dataclass
class ObstaclePair:
    x: float
    gap_y: int
    gap_height: int
    width: int
    active: bool = True
    scored: bool = False
    dynamic_offset: float = 0.0
    phase: float = 0.0

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

    def spawn(self, difficulty_level: int = 1) -> None:
        gap_height = random.randint(CONFIG.obstacle_gap_min, CONFIG.obstacle_gap_max)
        gap_y = random.randint(CONFIG.obstacle_margin_y, CONFIG.screen_height - CONFIG.obstacle_margin_y - gap_height)

        obstacle = ObstaclePair(
            x=CONFIG.screen_width + 30,
            gap_y=gap_y,
            gap_height=gap_height,
            width=CONFIG.obstacle_width,
            phase=random.uniform(0.0, math.pi * 2),
        )
        self.items.append(obstacle)

    def update(self, dt: float, scroll_speed: float) -> None:
        alive_items: list[ObstaclePair] = []
        for obstacle in self.items:
            obstacle.x -= scroll_speed * dt

            if CONFIG.dynamic_obstacles:
                obstacle.phase += dt * 1.6
                obstacle.dynamic_offset = math.sin(obstacle.phase) * 18.0
            else:
                obstacle.dynamic_offset = 0.0

            if obstacle.x + obstacle.width > 0:
                alive_items.append(obstacle)
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
            pygame.draw.rect(screen, (80, 210, 100), obstacle.top_rect())
            pygame.draw.rect(screen, (80, 210, 100), obstacle.bottom_rect())
