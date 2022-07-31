import os, pygame
from sys import exit

os.system('clear')
os.chdir('/Users/username/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Collisions With Rectangles:

We're going to check and see if one object's rectangle collide with any other rectangles
We can do this by typing: rect1.colliderect(rect2)
Or in our case: player_rectangle.collide(snail_rectangle)
It will simply return True or False/ 1 or 0

rect1.collidepoint((x,y))
Its pretty intuitive
Pretty much perfect when incorporating mouses

Getting the mouse's position:
Either pygame.mouse or event loop
pygame.mouse ---> mouse position, button, clicks, etc.
event loop ---> same as pygame.mouse but only when the mouse does something

event loop ---> 
pygame.MOUSEMOTION (Returns (x,y) when the mouse moves)
pygame.MOUSEBUTTONDOWN (Returns if the mouse button is pressed down)
pygame.MOUSEBUTTONUP (Returns if the mouse button is pressed down and then let go)


'''
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Big Balls')

sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)
text_surface = text_font.render('Welcome to Skyward', False, 'DarkGreen')

snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomleft = (800, 300))

player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png')
player_rectangle = player_surface.get_rect(midbottom = (100, 300))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # This is similar to pygame.mouse.get_pos except that this only gets the position if you move the mouse. If you don't then itll return nothing
        # This would be useful to lower the amount of data being outputed
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos):
        #         print('Collision')
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    screen.blit(snail_surface, snail_rectangle)
    snail_rectangle.x -= 2
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800
    screen.blit(player_surface, player_rectangle)

    # To start, we want to put the 'collision check' at the bottom
    # if player_rectangle.colliderect(snail_rectangle):
    #     player_rectangle.y += 10
    
    # To get our mouses position (x, y) constantly
    # mouse_position = pygame.mouse.get_pos()
    # Then we can check to see if it works
    # if player_rectangle.collidepoint(mouse_position):
         # player_rectangle.y -= 0
         # We can also check to see if we're pressing any mouse buttons (Left click(True/False), Middle click(True/False), Right Click(True/False))
         # print(pygame.mouse.get_pressed())



    pygame.display.update()
    clock.tick(60)
