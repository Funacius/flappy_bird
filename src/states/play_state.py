from __future__ import annotations

import pygame

from src.states.base_state import BaseState
from src.settings import CONFIG
from src.entities.player import Player
from src.entities.obstacle import ObstacleManager
from src.entities.collectible import CollectibleManager
from src.environment.background import ParallaxBackground
from src.environment.spawner import Spawner
from src.systems.collision import check_player_vs_obstacles, check_player_vs_collectibles
from src.systems.difficulty import DifficultyController
from src.systems.particles import ParticleSystem
from src.ui.hud import draw_hud


class PlayState(BaseState):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.background = ParallaxBackground()
        self.player = Player(CONFIG.player_x, CONFIG.player_start_y)
        self.obstacles = ObstacleManager()
        self.collectibles = CollectibleManager()
        self.spawner = Spawner(self.obstacles, self.collectibles)
        self.difficulty = DifficultyController()
        self.particles = ParticleSystem() if CONFIG.particle_effects else None

        self.score = 0
        self.alive = True

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player.flap()
                if self.particles:
                    self.particles.emit(self.player.x, self.player.y + self.player.height // 2)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.player.flap()
                if self.particles:
                    self.particles.emit(self.player.x, self.player.y + self.player.height // 2)

    def update(self, dt: float) -> None:
        if not self.alive:
            return

        self.difficulty.update_level(dt)
        scroll_speed = self.difficulty.current_speed(CONFIG.base_scroll_speed)
        self.background.update(dt, scroll_speed)
        self.player.update(dt)
        self.spawner.update(dt, scroll_speed, self.difficulty)
        self.obstacles.update(dt, scroll_speed)
        self.collectibles.update(dt, scroll_speed)
        if self.particles:
            self.particles.update(dt)

        if check_player_vs_obstacles(self.player, self.obstacles.items):
            self._game_over()
            return

        gained = check_player_vs_collectibles(self.player, self.collectibles.items)
        self.score += gained

        if self.player.y <= 0 or self.player.y + self.player.height >= (CONFIG.screen_height - CONFIG.ground_height):
            self._game_over()
            return

        self.score += self.obstacles.consume_passed(self.player.x)

    def _game_over(self) -> None:
        self.alive = False
        self.game.shared["last_score"] = self.score
        self.game.shared["best_score"] = max(self.game.shared["best_score"], self.score)
        self.game.change_state("game_over")

    def draw(self, screen: pygame.Surface) -> None:
        self.background.draw(screen)
        self.collectibles.draw(screen)
        self.obstacles.draw(screen)
        self.player.draw(screen)
        if self.particles:
            self.particles.draw(screen)
        draw_hud(screen, self.score, self.difficulty.level)
