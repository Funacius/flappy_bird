from __future__ import annotations
import pygame
import os

from src.core.base_entity import BaseEntity
from src.settings import CONFIG
from src.systems.animation import Animation
from src.systems.sfx import SFX


class Player(BaseEntity):
    def __init__(self, x: float, y: float) -> None:
        # Use the size from CONFIG
        super().__init__(x=x, y=y, width=CONFIG.player_width, height=CONFIG.player_height)

        self.velocity_y = 0.0
        self.is_flapping = False
        self.flap_timer = 0.0

        # 1. Load frames as separate files (Assuming you have plane_1.png, plane_2.png, etc.)
        # This is much more reliable than a SpriteSheet if you are a beginner!
        def load_plane_img(name):
            path = f"assets/images/{name}.png"
            if os.path.exists(path):
                img = pygame.image.load(path).convert_alpha()
                # Scale the image to fit the player width/height from settings
                return pygame.transform.scale(img, (self.width, self.height))
            return None

        # Try to load 3 frames of animation
        p1 = load_plane_img("planeRed1")
        p2 = load_plane_img("planeRed2")
        p3 = load_plane_img("planeRed3")

        # Fallback if files aren't found
        if not p1:
            p1 = pygame.Surface((self.width, self.height))
            p1.fill((200, 50, 50))

        # 2. Setup Animations
        # Idle uses frame 1 and 2 (slight wing movement)
        self.idle_animation = Animation([p1, p2 if p2 else p1], fps=8)
        # Flap uses frame 3 (wings fully down/up)
        self.flap_animation = Animation([p3 if p3 else p1], fps=1)

    def flap(self) -> None:
        self.velocity_y = CONFIG.flap_impulse
        self.is_flapping = True
        # Keep the "flap" frame visible for a bit longer to prevent flickering
        self.flap_timer = 0.25

        # 🔊 Play sound
        sfx = SFX.get_instance()
        if sfx:
            sfx.play("fly")

    def update(self, dt: float) -> None:
        # Physics
        self.velocity_y += CONFIG.gravity * dt
        self.y += self.velocity_y * dt

        # Animation State Logic
        if self.flap_timer > 0:
            self.flap_timer -= dt
            self.is_flapping = True
        else:
            self.is_flapping = False

        self.idle_animation.update(dt)
        self.flap_animation.update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        # Choose frame
        if self.is_flapping:
            frame = self.flap_animation.current_frame
        else:
            frame = self.idle_animation.current_frame

        # Add a slight rotation based on velocity (Classic Flappy Bird feel!)
        # This makes the game feel much more "polished"
        rotation = -self.velocity_y * 0.05
        rotation = max(-30, min(30, rotation))  # Limit rotation
        rotated_frame = pygame.transform.rotate(frame, rotation)

        # Draw centered
        dest_rect = rotated_frame.get_rect(center=(int(self.x + self.width / 2), int(self.y + self.height / 2)))
        screen.blit(rotated_frame, dest_rect)