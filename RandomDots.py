import pygame
pygame.init()
import random
screen=pygame.display.set_mode([1850,1000])
pygame.display.set_caption("RANDOM DOTS")
keep_going=True
count=0
while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
    count=count+1
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    posx=random.randint(0,1850)
    posy=random.randint(0,1000)
    rad=random.randint(10,100)
    pygame.draw.circle(screen,(r,g,b),(posx,posy),rad)
    pygame.display.update()
print(count)    
pygame.quit()    
