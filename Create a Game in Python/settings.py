import pygame as pg

class Settings:
    def __init__(self):
        screen_info = pg.display.Info()
        self.screen_width = screen_info.current_w
        self.screen_height = screen_info.current_h
        self.bg_color = (230, 230, 230)
        self.flag = pg.RESIZABLE

        # Initialize static settings
        self.apples_allowed = 3
        self.apple_limit = 3
        self.game_over = False

        # Scoring
        self.apple_points = 2

        # Levelup Scale
        self.levelup_scale = 1.1

        self.initialize_dynamic_settings()