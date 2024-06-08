import pygame, math, sys

def setup():
    pygame.init()
    res = (300, 300)
    screen = pygame.display.set_mode(res)
    circles_pos = [(150, 100), (0,0), (200, 200)]
    clock = pygame.time.Clock()
    blue_pos_x = 0
    b = 0
    step =1
    return res, screen, circles_pos, clock, blue_pos_x, b, step

res, screen, circles_pos, clock, blue_pos_x, b, step = setup()


while True:
    screen.fill((255, 0, 0))
    
    for cp in circles_pos:
    
        pygame.draw.circle(screen, (0, 0, 0), cp , 15)

    pos = (blue_pos_x, 120+ 30*math.sin(blue_pos_x/15))
    pygame.draw.circle(screen, (0, 0, b), pos , 15)
    
    b += step
    blue_pos_x += 1
    
    if blue_pos_x == 220:
        blue_pos_x = 0    
    if b > 254:
        step = -1
    if b == 0:
        step = 1
    
    pygame.display.flip()
    clock.tick(70)

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Bye!")
            sys.exit()
            

