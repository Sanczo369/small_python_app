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
