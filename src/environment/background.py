from __future__ import annotations
import pygame
from src.settings import CONFIG


class ParallaxLayer:
    def __init__(self, image_path: str, relative_speed: float, y: int) -> None:
        self.image = pygame.image.load(image_path).convert_alpha()
        self.width = self.image.get_width()
        self.relative_speed = relative_speed
        self.y = y
        self.offset = 0.0

    def update(self, dt: float, scroll_speed: float) -> None:
        self.offset = (self.offset + scroll_speed * self.relative_speed * dt) % self.width

    def draw(self, screen: pygame.Surface) -> None:
        x = -self.offset
        while x < CONFIG.screen_width:
            screen.blit(self.image, (int(x), self.y))

            # Fill the gap below the ground layer (relative_speed 1.0)
            if self.relative_speed >= 1.0:
                # Draw a brown rectangle to fill the bottom of the screen
                pygame.draw.rect(screen, (189, 148, 108),
                                 (int(x), self.y + self.image.get_height() - 2,
                                  self.width + 2, CONFIG.screen_height - self.y))
            x += self.width


class ParallaxBackground:
    def __init__(self) -> None:
        # Ensure these files exist in assets/images/
        self.layers = [
            ParallaxLayer("assets/images/sky.png", 0.15, 0),
            ParallaxLayer("assets/images/mountains.png", 0.35, 180),
            ParallaxLayer("assets/images/ground.png", 1.00, CONFIG.screen_height - 100),
        ]

    def update(self, dt: float, scroll_speed: float) -> None:
        for layer in self.layers:
            layer.update(dt, scroll_speed)

    def draw(self, screen: pygame.Surface) -> None:
        # ParallaxBackground should NOT have an offset.
        # It just calls the draw method of each layer.
        for layer in self.layers:
            layer.draw(screen)