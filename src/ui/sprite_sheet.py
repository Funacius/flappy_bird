import pygame


class SpriteSheet:
    def __init__(self, filename: str) -> None:
        """Load the sprite sheet image."""
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

    def get_image(self, x: int, y: int, width: int, height: int, scale: float = 1.0) -> pygame.Surface:
        """Extracts a single frame from the sprite sheet."""
        # Create a blank surface with transparent background
        image = pygame.Surface((width, height), pygame.SRCALPHA)

        # Blit (copy) the specific region from the sprite sheet onto the blank surface
        image.blit(self.sheet, (0, 0), (x, y, width, height))

        # Scale the image if necessary
        if scale != 1.0:
            image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        return image