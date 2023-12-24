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

run=True
while run:
    screen.fill(white)
    pygame.draw.rect(screen,green,pygame.Rect(0,0,180,1280))
    pygame.draw.rect(screen,green,pygame.Rect(540,0,180,1280))
    pygame.draw.rect(screen,blue,pygame.Rect(x,y,40,80))
    pygame.draw.rect(screen,blue,pygame.Rect(a,b,40,80))
    pygame.draw.rect(screen,red,pygame.Rect(e,f,40,80))

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                e-=cha
            if event.key==pygame.K_p:
                e+=cha
    y+=ch
    b+=ch

    if y>=640:
        x=random.randint(180,500)
        y=random.randint(0,200)
        score_value+=1


    if b>=640:
        x=random.randint(180,500)
        y=random.randint(0,200)
        score_value+=1


    if abs(y-f)<100 and abs(x-e)<6:
        game_over()
        score_value=0

    if abs(a-e)<100 and abs(b-f)<6:
        game_over()
        score_value=0

    show_score()
    pygame.display.update()