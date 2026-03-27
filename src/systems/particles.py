from __future__ import annotations

from dataclasses import dataclass
import random
import pygame


@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    ttl: float


class ParticleSystem:
    def __init__(self) -> None:
        self.particles: list[Particle] = []

    def emit(self, x: float, y: float, count: int = 8) -> None:
        for _ in range(count):
            self.particles.append(
                Particle(
                    x=x,
                    y=y,
                    vx=random.uniform(-120, -20),
                    vy=random.uniform(-60, 60),
                    ttl=random.uniform(0.25, 0.55),
                )
            )

    def update(self, dt: float) -> None:
        alive: list[Particle] = []
        for p in self.particles:
            p.ttl -= dt
            p.x += p.vx * dt
            p.y += p.vy * dt
            if p.ttl > 0:
                alive.append(p)
        self.particles = alive

    def draw(self, screen: pygame.Surface) -> None:
        for p in self.particles:
            alpha = max(0, min(255, int(255 * p.ttl / 0.55)))
            surf = pygame.Surface((6, 6), pygame.SRCALPHA)
            pygame.draw.circle(surf, (255, 180, 80, alpha), (3, 3), 3)
            screen.blit(surf, (p.x, p.y))
