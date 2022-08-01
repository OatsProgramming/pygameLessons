import pygame, os
from sys import exit

os.system('clear')
os.chdir('/Users/username/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
State management in Pygame:

if game_active:
    current game
else:
    game_over

A pretty simple concept. Not ideal for higher complexities
'''

pygame.init()

# We'll first create variable that returns whether True or not
game_active = True

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Skyward')

sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)

welcome_surface = text_font.render('Welcome to Skyward', False, 'DarkGreen')
welcome_rect = welcome_surface.get_rect(center = (400, 100))

score_surface = text_font.render('Score: ', False, 'DarkGrey')
score_rect = score_surface.get_rect(center = (400, -100))

snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))
player_gravity = 0

# We'll incorporate a 'Play Again?' text

playagain = text_font.render('Press Space to play again', False, 'Black')
playagain_rect = playagain.get_rect(center = (400, 200))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # We essentially do the same here as we do below
        # But we're going to check to see if the player wants to play again
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity -= 20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity -= 20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

        
        
    
    # We'll create an if statement here
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(welcome_surface, welcome_rect)
        welcome_rect.y -= 2

        screen.blit(score_surface, score_rect)
        if welcome_rect.bottom <= 0:
            score_rect.y = 100

        snail_rect.x -= 3
        screen.blit(snail_surface, snail_rect)
        if snail_rect.right <= 0:
            snail_rect.left = 800

        player_gravity += 1
        player_rect.y += player_gravity
        screen.blit(player_surface, player_rect)

        if player_rect.bottom >= 300:
            player_gravity = 0
            player_rect.bottom = 300

        # Here is where we'll implement game over
        if player_rect.colliderect(snail_rect):
            game_active = False

    # This is the other section of the game. Could be the intro or game over or whatever
    else:
        screen.fill('yellow')
        screen.blit(playagain, playagain_rect)
    pygame.display.update()
    clock.tick(60)
        

    
