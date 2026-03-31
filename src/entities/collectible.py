from __future__ import annotations
from dataclasses import dataclass
import pygame

from src.systems.animation import Animation
from src.core.object_pool import ObjectPool


@dataclass
class Collectible:
    x: float = 0.0
    y: float = 0.0
    size: int = 24
    active: bool = True

    # Add a reset method for the Object Pool
    def reset(self, x: float, y: float):
        self.x = x
        self.y = y
        self.active = True

    def rect(self) -> pygame.Rect:
        return pygame.Rect(int(self.x), int(self.y), self.size, self.size)


class CollectibleManager:
    def __init__(self) -> None:
        self.items: list[Collectible] = []

        # 1. Load the 10 separate frames in a loop
        coin_frames = []
        for i in range(1, 11):  # Assuming files are named coin_1.png to coin_10.png
            try:
                # Load each image file
                img = pygame.image.load(f"assets/images/coin/coin{i}.png").convert_alpha()
                # Scale it to the right size (e.g., 24x24 pixels)
                img = pygame.transform.scale(img, (24, 24))
                coin_frames.append(img)
            except pygame.error:
                print(f"Warning: Could not find assets/images/coin/coin{i}.png")

        # 2. Create the animation with the loaded frames
        self.anim = Animation(frames=coin_frames, fps=12)

        # 3. Initialize the Object Pool for collectibles
        self.pool: ObjectPool[Collectible] = ObjectPool(lambda: Collectible(), initial_size=10)

    def spawn(self, x: float, y: float) -> None:
        # ACQUIRE from pool instead of creating new
        item = self.pool.acquire()
        item.reset(x, y)
        self.items.append(item)

    def update(self, dt: float, scroll_speed: float) -> None:
        self.anim.update(dt)
        alive_items: list[Collectible] = []

        for item in self.items:
            item.x -= scroll_speed * dt

            # If still on screen and not collected, keep it. 
            # Otherwise, RELEASE to pool.
            if item.x + item.size > 0 and item.active:
                alive_items.append(item)
            else:
                self.pool.release(item)  # <-- Return to pool!

        self.items = alive_items

    def draw(self, screen: pygame.Surface) -> None:
        frame = self.anim.current_frame
        for item in self.items:
            screen.blit(frame, (item.x, item.y))