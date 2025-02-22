import pygame.font
from apple import Apple
from pygame.sprite import Group

class Scoreboard:
    def __init__(self, ac_game):
        self.ac_game = ac_game
        self.screen = ac_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ac_game.settings
        self.stats = ac_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_apples()
        self.prep_level()