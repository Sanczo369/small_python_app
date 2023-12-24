import pygame
import random

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

x = random.randint(180,500)
y = random.randint(0,200)
a = random.randint(180,500)
b = random.randint(0,200)

e = 350
f = 600
ch = 3
cha = 5

screen = pygame.display.set_mode((720,1280))
score_value = 0
font2 = pygame.font.Font('freesansbold.ttf',50)
font1 = pygame.font.Font("freesansbold.ttf",50)

def show_score():
    score=font2.render("Score: "+ str(score_value),True,(0,255,0))
    screen.blit(score,(10,10))

def game_over():
    over_text=font1.render("GAME OVER", True, (0,255,255))
    screen.blit(over_text,(200,400))
