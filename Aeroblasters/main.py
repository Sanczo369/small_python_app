# Aeroblasters

# Author : Prajjwal Pathak (pyguru)
# Date : Thursday, 30 September, 2021

import random
import pygame
from objects import Background, Player, Enemy, Bullet, Explosion, Fuel, \
					Powerup, Button, Message, BlinkingText

pygame.init()
SCREEN = WIDTH, HEIGHT = 288, 512

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60