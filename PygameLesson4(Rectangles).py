import pygame, os
from sys import exit

os.system('clear')
os.chdir('/Users/jaliljusay/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
For next lesson, we'll focus on RECTANGLES:

They will help precise positioning on surfaces
Also will help detect collisions

Surface for image info ---> Placement via rectangles

Think abt adobe after effects and origin points
'''

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Suck on deez nuts')

sky_surface = pygame.image.load('graphics for tutorial/Sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/Ground.png').convert()
snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (900, 300))
# snail_x_position = 900
text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)
text_surface = text_font.render('Welcome to Skyward', False, 'DarkGreen')

# We'll start off by loading the player image
player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
# This is one way to create a rectangle:
# player_rectangle = pygame.Rect()

# But this would be the most sufficient way to do so
# Takes the surface and draws a rectangle around it
# Theres multiple points you can use: topleft, midleft, topright, midright, center, etc. It all depends on you and the situation
# For this scenario, we want to put the point of origin on the middle bottom so that way we can align more easily with the ground
# Just put the same y input as the ground surface to make the player touch the ground
player_rectangle = player_surface.get_rect(midbottom = (100, 300))

# Eventually, we will create a sprite class to avoid the tedious work of making the surface and the rectangle multiple times 


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    # We can do the same for the snail
    #           screen.blit(snail_surface, (snail_surface.get_rect(midbottom = (snail_x_position, 300))))
    #           snail_x_position -= 2
    #           if snail_x_position == -50:
    #               snail_x_position = 900
    # However, there's a much more code efficient way to do this

    screen.blit(snail_surface, snail_rectangle)
    snail_rectangle.x -= 2
    if snail_rectangle.right < 0:
        snail_rectangle.left = 800

    # screen.blit(player_surface, (80, 275))
    # Now we can just put the player_rectangle for the player's position
    screen.blit(player_surface, player_rectangle)
    screen.blit(text_surface, (370, 50))

    pygame.display.update()
    clock.tick(60)