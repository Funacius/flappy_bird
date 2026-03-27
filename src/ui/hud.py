import pygame


def draw_hud(screen: pygame.Surface, score: int, difficulty_level: int) -> None:
    font = pygame.font.SysFont("arial", 28, bold=True)
    score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
    level_surf = font.render(f"Level: {difficulty_level}", True, (255, 255, 255))
    screen.blit(score_surf, (16, 14))
    screen.blit(level_surf, (16, 46))
