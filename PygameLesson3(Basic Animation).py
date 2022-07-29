import os, pygame
from sys import exit

os.system('clear')
os.chdir('/Users/jaliljusay/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Essentially, w/o changing anything from the prior lesson, the image we see on the display seems static
However, it is constantly being updated at 60 fps. So, we need to incorporate some slight movement to create
a proper animation
'''

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Skyward')

# TIP: add .convert() at the end to make the game run faster as itll make it easier for pygame
# For the snail, we used .convert_alpha() due to the fact the snail1.png has a white background attached

sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_x_position = 600

test_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)
text_surface = test_font.render('My game', False, 'DarkGreen')

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 50))
    # The following is to make it move. Its on default by 600
    snail_x_position -= 2
    screen.blit(snail_surface, (snail_x_position, 265))
    # Its pretty intuitive from here
    if snail_x_position == -100:
        snail_x_position = 900

    pygame.display.update()
    clock.tick(60)