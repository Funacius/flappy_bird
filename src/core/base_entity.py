from __future__ import annotations

from dataclasses import dataclass
import pygame


@dataclass
class BaseEntity:
    x: float
    y: float
    width: int
    height: int
    active: bool = True

    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def update(self, dt: float) -> None:
        raise NotImplementedError

    def draw(self, screen: pygame.Surface) -> None:
        raise NotImplementedError
