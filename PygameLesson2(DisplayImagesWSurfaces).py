import pygame
from sys import exit
import os

os.system('clear')

'''
In order to draw on our display, we must create a surface

There are two kinds of surfaces:
Display surface: the one that we've made already; just a game window; essentially the canvas
Regular surface: Needs to placed on the display surface; essentially the image; will not be visible if not attached to the display surface
'''

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Big PP')

clock = pygame.time.Clock()

width2 = 100
height2 = 200
# Regular Surface: we'll make a plain text surface for now
test_surface = pygame.Surface((width2, height2))
# The following is to change the test_surface color. There's a whole list of other colors; search up pygame fill colors
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # blit: Block image tranfer (essentially to put an image on top on the display)
    # This is to help attach the test_surface to the display
    # If you were to say screen.blit(test_surface(0,0)), then you would see the test_surface is on the top left corner.
    # Thats bc if you think of it as a graph its essentially setting it at x: 0 and y: 0. 
    # However, the graph is y axis inverted: so to go down, you must add y.
    # So essentially, we're saying that we want to get the top left of the test_surface onto the top left of the display
    # Note: its (test_surface, (x,y)) not test_surface(x,y)
    screen.blit(test_surface, (0,0))
    
    pygame.display.update()
    clock.tick(60)






