import pygame


def draw_hud(screen: pygame.Surface, score: int, difficulty_level: int) -> None:
    font = pygame.font.SysFont("arial", 28, bold=True)

    def draw_with_shadow(text, pos):
        # Draw black shadow first
        shadow = font.render(text, True, (0, 0, 0))
        screen.blit(shadow, (pos[0] + 2, pos[1] + 2))
        # Draw white text on top
        surf = font.render(text, True, (255, 255, 255))
        screen.blit(surf, pos)

    draw_with_shadow(f"Score: {score}", (16, 14))
    draw_with_shadow(f"Level: {difficulty_level}", (16, 46))
