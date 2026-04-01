import pygame
import os

class SFX:
    _instance = None   # 👈 static reference

    def __init__(self):
        if SFX._instance is not None:
            return  # prevent re-init

        pygame.mixer.init()

        base_path = os.path.join("assets", "sfx")

        self.sounds = {
            "fly": pygame.mixer.Sound(os.path.join(base_path, "plr_sfx.wav")),
            "click": pygame.mixer.Sound(os.path.join(base_path, "click_sfx.wav")),
            "coin": pygame.mixer.Sound(os.path.join(base_path, "coin_sfx.wav")),
        }

        self.sounds["fly"].set_volume(0.3)
        self.sounds["click"].set_volume(0.7)
        self.sounds["coin"].set_volume(0.3)

        SFX._instance = self

    @staticmethod
    def get_instance():
        return SFX._instance

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].stop()
            self.sounds[name].play()

    def play_music(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.6)