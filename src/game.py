import pygame

from src.settings import CONFIG
from src.states.menu_state import MenuState
from src.states.play_state import PlayState
from src.states.game_over_state import GameOverState
from src.systems.sfx import SFX


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((CONFIG.screen_width, CONFIG.screen_height))
        pygame.display.set_caption(CONFIG.title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.shared = {
            "best_score": 0,
            "last_score": 0,
        }
        self.state = MenuState(self)

        self.sfx = SFX()
        self.sfx.play_music("assets/sfx/bg_music.mp3")

    def change_state(self, state_name: str) -> None:
        if state_name == "menu":
            self.state = MenuState(self)
        elif state_name == "play":
            self.state = PlayState(self)
        elif state_name == "game_over":
            self.state = GameOverState(self)
        else:
            raise ValueError(f"Unknown state: {state_name}")

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick(CONFIG.fps) / 1000.0
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.state.handle_events(events)
            self.state.update(dt)
            self.state.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
