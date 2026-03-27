from __future__ import annotations

import pygame


class Animation:
    def __init__(self, frames: list[pygame.Surface], fps: float) -> None:
        self.frames = frames
        self.fps = fps
        self.frame_time = 1.0 / fps if fps > 0 else 1.0
        self.time_accumulator = 0.0
        self.index = 0

    @property
    def current_frame(self) -> pygame.Surface:
        return self.frames[self.index]

    def update(self, dt: float) -> None:
        if not self.frames:
            return

        self.time_accumulator += dt
        while self.time_accumulator >= self.frame_time:
            self.time_accumulator -= self.frame_time
            self.index = (self.index + 1) % len(self.frames)
