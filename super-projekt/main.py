import sys

import pygame
from colors import c
pygame.init()

screen_size = 800, 600
screen = pygame.display.set_mode(screen_size)
screen_center = (screen_size[0] // 2), (screen_size[1] // 2)
pygame.display.set_caption("Adventures of Blue Bartłomiej")

x, y = screen_center
speed = 0.2

playing = True
print("This is a game with adventures of Blue Bartlomiej!")


def check_boundaries():
    global x
    global y
    if x > screen_size[0]:
        x = screen_size[0]
    elif x < 0:
        x = 0
    if y > screen_size[1]:
        y = screen_size[1]
    elif y < 0:
        y = 0


while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            print("Bartłomiej: Bye")

    keys = pygame.key.get_pressed()
    speed_multiplier = 2 if keys[pygame.K_LSHIFT] else 1

    if keys[pygame.K_q] or keys[pygame.K_x]:
        playing = False
        print("Bartłomej says BYE !")
        sys.exit(0)

    if keys[pygame.K_w]:
        y -= speed * speed_multiplier
    if keys[pygame.K_s]:
        y += speed * speed_multiplier
    if keys[pygame.K_a]:
        x -= speed * speed_multiplier
    if keys[pygame.K_d]:
        x += speed * speed_multiplier
    check_boundaries()

    screen.fill(c.black)
    pygame.draw.circle(screen, c.blue, (x, y), 50)
    pygame.display.flip()
