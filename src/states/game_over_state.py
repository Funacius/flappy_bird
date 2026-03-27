import pygame

from src.states.base_state import BaseState
from src.ui.text import draw_centered_text


class GameOverState(BaseState):
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.game.change_state("play")
                elif event.key == pygame.K_ESCAPE:
                    self.game.running = False

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((28, 18, 18))
        score = self.game.shared["last_score"]
        best = self.game.shared["best_score"]
        draw_centered_text(screen, "GAME OVER", 56, y_offset=-70)
        draw_centered_text(screen, f"Score: {score}", 30, y_offset=0)
        draw_centered_text(screen, f"Best: {best}", 26, y_offset=40)
        draw_centered_text(screen, "Press R to restart", 24, y_offset=95)
