from __future__ import annotations
import pygame


class BaseState:
    def __init__(self, game) -> None:
        self.game = game

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        pass
