import pygame

from src.states.base_state import BaseState
from src.ui.text import draw_centered_text
from src.systems.sfx import SFX


class MenuState(BaseState):
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #Play sound
                sfx = SFX.get_instance()
                if sfx:
                    sfx.play("click")
                self.game.change_state("play")
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #Play sound
                sfx = SFX.get_instance()
                if sfx:
                    sfx.play("click")
                self.game.change_state("play")

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((15, 20, 35))
        draw_centered_text(screen, "INFINITE FLYER", 60, y_offset=-50)
        draw_centered_text(screen, "Press SPACE or Left Click to Start", 28, y_offset=20)
