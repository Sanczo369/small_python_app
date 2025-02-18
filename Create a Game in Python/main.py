import pygame as pg
import sys
from apple import Apple
from settings import Settings
from basket import Basket
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from sounds import Music

class AppleCatcher:
    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, \
        self.settings.screen_height), self.settings.flag)
        pg.display.set_caption('Apple Catcher Game')

        # Background Window Image
        self.background = pg.image.load('Images/background.png')

        self.music = Music()

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.basket = Basket(self)
        self.apples = pg.sprite.Group()
        # Make the Play button
        self.play_button = Button(self, "Play")

        # Getting the Screen's Rectangular
        self.screen_rect = self.screen.get_rect()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.basket.update()
                self._drop_apples()
                self.apples.update()
                self._check_apples_bottom()
                self._update_apples()
            self._update_screen()

    def check_for_level_up(self):
        # The game level up when the scores reach multiple of 20.
        if self.stats.score!=0 and self.stats.score%20 == 0:
            self.settings.increase_speed()
            # Increase Level
            self.stats.level += 1
            self.sb.prep_level()