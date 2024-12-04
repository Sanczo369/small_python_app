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

# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 20)

# IMAGES **********************************************************************

plane_img = pygame.image.load('Assets/plane.png')
logo_img = pygame.image.load('Assets/logo.png')
fighter_img = pygame.image.load('Assets/fighter.png')
clouds_img = pygame.image.load('Assets/clouds.png')
clouds_img = pygame.transform.scale(clouds_img, (WIDTH, 350))

home_img = pygame.image.load('Assets/Buttons/homeBtn.png')
replay_img = pygame.image.load('Assets/Buttons/replay.png')
sound_off_img = pygame.image.load("Assets/Buttons/soundOffBtn.png")
sound_on_img = pygame.image.load("Assets/Buttons/soundOnBtn.png")

# BUTTONS *********************************************************************

home_btn = Button(home_img, (24, 24), WIDTH // 4 - 18, HEIGHT//2 + 120)
replay_btn = Button(replay_img, (36,36), WIDTH // 2  - 18, HEIGHT//2 + 115)
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT//2 + 120)