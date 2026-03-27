import pygame

from src.settings import CONFIG


def draw_centered_text(screen: pygame.Surface, text: str, size: int, y_offset: int = 0) -> None:
    font = pygame.font.SysFont("arial", size, bold=True)
    surf = font.render(text, True, (255, 255, 255))
    rect = surf.get_rect(center=(CONFIG.screen_width // 2, CONFIG.screen_height // 2 + y_offset))
    screen.blit(surf, rect)
