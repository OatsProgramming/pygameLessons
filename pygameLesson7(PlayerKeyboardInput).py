import os, pygame
from sys import exit

os.system('clear')
os.chdir('/Users/username/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Player Keyboard Input:
Same as Mouse
pygame.key or event loop

Event loop:
1) checks if any button was pressed
2) work with a specific key

For the mouse and keyboard inputs, why do we have two different methods to get the same input?
When using classes, you want the controls inside of the relevant classes

For general things, such as closing the game, the event loop is the ideal place.
'''

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('SkyWard')

sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)

welcome_surface = text_font.render('Welcome to Skyward', False, 'DarkGreen')
welcome_rectangle = welcome_surface.get_rect(center = (400, 100))

score_surface = text_font.render('Score: ', False, 'DarkGrey')
score_rectangle = score_surface.get_rect(center = (400, -100))

snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png')
snail_rectangle = snail_surface.get_rect(bottomleft = (800, 300))

player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png')
player_rectangle = player_surface.get_rect(midbottom = (100, 300))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos):
                print(event.pos)

        # Similar to pygame.MOUSEBUTTONDOWN
        if event.type == pygame.KEYDOWN:
            # if we want to know which key is being pressed
            if event.key == pygame.K_SPACE:
                print('Jump')
        
        # Similar to pygame.MOUSEBUTTONUP
        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(welcome_surface, welcome_rectangle)
    welcome_rectangle.y -= 2
    if welcome_rectangle.bottom <= 0:
        score_rectangle.y = 50   

    pygame.draw.rect(screen, '#CEE5E4', score_rectangle)
    pygame.draw.rect(screen, '#ABD6D5', score_rectangle, 10)
    screen.blit(score_surface, score_rectangle)

    screen.blit(snail_surface, snail_rectangle)
    snail_rectangle.x -= 2
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800

    screen.blit(player_surface, player_rectangle)

    # This is where we will make the character move via input
    # This will return all buttons and its current state (similar to pygame.mouse.get_pos())
    # We will treat it as a dictionary
    # keys = pygame.key.get_pressed()
    # In order to figure out which key we would like to mess with, refer to the pygame library online
    # But, its usually just pygame.K_"insert whatever key here") KEYWORD: USUALLY
    # if keys[pygame.K_SPACE]:
    #     print('Jump')

    
    if player_rectangle.colliderect(snail_rectangle):
        player_rectangle.y -= 2
    elif not player_rectangle.colliderect(snail_rectangle):
        if player_rectangle.bottom != 300:
            player_rectangle.y += 2
   
    
    pygame.display.update()
    clock.tick(60)

