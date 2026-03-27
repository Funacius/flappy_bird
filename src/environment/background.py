from __future__ import annotations

import pygame

from src.settings import CONFIG


class ParallaxLayer:
    def __init__(self, color: tuple[int, int, int], height: int, relative_speed: float, y: int) -> None:
        self.color = color
        self.height = height
        self.relative_speed = relative_speed
        self.y = y
        self.offset = 0.0
        self.segment_width = CONFIG.screen_width

    def update(self, dt: float, scroll_speed: float) -> None:
        self.offset = (self.offset + scroll_speed * self.relative_speed * dt) % self.segment_width

    def draw(self, screen: pygame.Surface) -> None:
        x1 = -self.offset
        x2 = x1 + self.segment_width
        rect1 = pygame.Rect(int(x1), self.y, self.segment_width, self.height)
        rect2 = pygame.Rect(int(x2), self.y, self.segment_width, self.height)
        pygame.draw.rect(screen, self.color, rect1)
        pygame.draw.rect(screen, self.color, rect2)


class ParallaxBackground:
    def __init__(self) -> None:
        self.sky_color = (120, 180, 255)
        self.layers = [
            ParallaxLayer((200, 230, 255), 80, 0.15, 60),
            ParallaxLayer((120, 150, 210), 120, 0.35, 190),
            ParallaxLayer((90, 110, 70), 100, 1.00, CONFIG.screen_height - 100),
        ]

    def update(self, dt: float, scroll_speed: float) -> None:
        for layer in self.layers:
            layer.update(dt, scroll_speed)

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill(self.sky_color)
        for layer in self.layers:
            layer.draw(screen)
