from __future__ import annotations

import pygame

from src.core.base_entity import BaseEntity
from src.settings import CONFIG
from src.systems.animation import Animation


class Player(BaseEntity):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x=x, y=y, width=CONFIG.player_width, height=CONFIG.player_height)
        self.velocity_y = 0.0

        idle_frames = [self._make_frame((255, 220, 80)), self._make_frame((255, 200, 60))]
        flap_frames = [self._make_frame((120, 255, 140)), self._make_frame((80, 230, 120))]
        self.idle_animation = Animation(idle_frames, fps=6)
        self.flap_animation = Animation(flap_frames, fps=12)
        self.is_flapping = False
        self.flap_timer = 0.0

    def _make_frame(self, color: tuple[int, int, int]) -> pygame.Surface:
        surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.ellipse(surf, color, (0, 0, self.width, self.height))
        pygame.draw.circle(surf, (20, 20, 20), (self.width - 15, 14), 4)
        return surf

    def flap(self) -> None:
        self.velocity_y = CONFIG.flap_impulse
        self.is_flapping = True
        self.flap_timer = 0.18

    def update(self, dt: float) -> None:
        self.velocity_y += CONFIG.gravity * dt
        self.y += self.velocity_y * dt

        self.flap_timer = max(0.0, self.flap_timer - dt)
        self.is_flapping = self.flap_timer > 0

        self.idle_animation.update(dt)
        self.flap_animation.update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        frame = self.flap_animation.current_frame if self.is_flapping else self.idle_animation.current_frame
        screen.blit(frame, (self.x, self.y))
