from __future__ import annotations

from dataclasses import dataclass
import pygame

from src.systems.animation import Animation


@dataclass
class Collectible:
    x: float
    y: float
    size: int = 24
    active: bool = True

    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x), int(self.y), self.size, self.size)


class CollectibleManager:
    def __init__(self) -> None:
        self.items: list[Collectible] = []
        self.anim = Animation(
            frames=[self._frame(8), self._frame(10), self._frame(12), self._frame(10)],
            fps=10,
        )

    def _frame(self, radius: int) -> pygame.Surface:
        size = 24
        surf = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 220, 80), (size // 2, size // 2), radius)
        return surf

    def spawn(self, x: float, y: float) -> None:
        self.items.append(Collectible(x=x, y=y))

    def update(self, dt: float, scroll_speed: float) -> None:
        self.anim.update(dt)
        alive_items: list[Collectible] = []
        for item in self.items:
            item.x -= scroll_speed * dt
            if item.x + item.size > 0 and item.active:
                alive_items.append(item)
        self.items = alive_items

    def draw(self, screen: pygame.Surface) -> None:
        frame = self.anim.current_frame
        for item in self.items:
            screen.blit(frame, (item.x, item.y))
