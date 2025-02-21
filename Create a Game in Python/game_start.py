class GameStats:
    '''Track statistics for Apple Catcher.'''
    def __init__(self, ac_game):
        self.settings = ac_game.settings
        self.game_active = False
        self.reset_stats()