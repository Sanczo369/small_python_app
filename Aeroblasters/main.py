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

# FONTS ***********************************************************************

game_over_font = 'Fonts/ghostclan.ttf'
tap_to_play_font = 'Fonts/BubblegumSans-Regular.ttf'
score_font = 'Fonts/DalelandsUncialBold-82zA.ttf'
final_score_font = 'Fonts/DroneflyRegular-K78LA.ttf'

game_over_msg = Message(WIDTH//2, 230, 30, 'Game Over', game_over_font, WHITE, win)
score_msg = Message(WIDTH-50, 28, 30, '0', final_score_font, RED, win)
final_score_msg = Message(WIDTH//2, 280, 30, '0', final_score_font, RED, win)
tap_to_play_msg = tap_to_play = BlinkingText(WIDTH//2, HEIGHT-60, 25, "Tap To Play",
				 tap_to_play_font, WHITE, win)

# SOUNDS **********************************************************************

player_bullet_fx = pygame.mixer.Sound('Sounds/gunshot.wav')
click_fx = pygame.mixer.Sound('Sounds/click.mp3')
collision_fx = pygame.mixer.Sound('Sounds/mini_exp.mp3')
blast_fx = pygame.mixer.Sound('Sounds/blast.wav')
fuel_fx = pygame.mixer.Sound('Sounds/fuel.wav')

pygame.mixer.music.load('Sounds/Defrini - Spookie.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

# GROUPS & OBJECTS ************************************************************

bg = Background(win)
p = Player(144, HEIGHT - 100)

enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()

# FUNCTIONS *******************************************************************

def shoot_bullet():
	x, y = p.rect.center[0], p.rect.y

	if p.powerup > 0:
		for dx in range(-3, 4):
			b = Bullet(x, y, 4, dx)
			player_bullet_group.add(b)
		p.powerup -= 1
	else:
		b = Bullet(x-30, y, 6)
		player_bullet_group.add(b)
		b = Bullet(x+30, y, 6)
		player_bullet_group.add(b)
	player_bullet_fx.play()

def reset():
	enemy_group.empty()
	player_bullet_group.empty()
	enemy_bullet_group.empty()
	explosion_group.empty()
	fuel_group.empty()
	powerup_group.empty()

	p.reset(p.x, p.y)

# VARIABLES *******************************************************************

level = 1
plane_destroy_count = 0
plane_frequency = 5000
start_time = pygame.time.get_ticks()

moving_left = False
moving_right = False

home_page = True
game_page = False
score_page = False

score = 0
sound_on = True

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False

		if event.type == pygame.KEYDOWN and game_page:
			if event.key == pygame.K_LEFT:
				moving_left = True
			if event.key == pygame.K_RIGHT:
				moving_right = True
			if event.key == pygame.K_SPACE:
				shoot_bullet()