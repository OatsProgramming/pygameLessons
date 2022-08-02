import pygame, os
from sys import exit

os.system('clear')
os.chdir('/Users/jaliljusay/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Displaying the score (time):

To measure time:
pygame.time.get_ticks()
--> Measures time in milliseconds since the game has started (pygame.init())

Goal:
1) Update score on every frame 
2) Put that on a surface
3) Display that surface

'''

# We'll first start off with creating a new function
def display_score():
    # divide by 1000 since its in milliseconds but do // instead of / to get actual integers instead of floats
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score_surface = text_font.render(f'Score: {current_time}', False, 'DarkGrey')
    score_rect = score_surface.get_rect(center = (400, 100))
    screen.blit(score_surface, score_rect)

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Skyward')

game_active = True

sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)

welcome_surface = text_font.render('Welcome to Skyward', False, 'DarkGreen')
welcome_rect = welcome_surface.get_rect(center = (400, 100))

# Start time will be set to 0 and wont change until we reboot the game to restart the current timer
start_time = 0

# score_surface = text_font.render('Score: ', False, "DarkGrey")
# score_rect = score_surface.get_rect(center = (400, -100))

playagain = text_font.render('Press Space to play again', False, 'Black')
playagain_rect = playagain.get_rect(center = (400, 200))

snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))
player_gravity = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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
                # This how we will restart the timer back to 0
                start_time = pygame.time.get_ticks() // 1000


    if game_active:

        screen.blit(sky_surface, (0,0))
        display_score()
        screen.blit(ground_surface, (0, 300))
        screen.blit(welcome_surface, welcome_rect)
        welcome_rect.y -= 2

        # screen.blit(score_surface, score_rect)
        # if welcome_rect.bottom <= 0:
            # score_rect.y = 100
        
        screen.blit(snail_surface, snail_rect)
        snail_rect.x -= 3
        if snail_rect.right <= 0:
            snail_rect.left = 800
        
        screen.blit(player_surface, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_gravity = 0
            player_rect.bottom = 300
        
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill('yellow')
        screen.blit(playagain, playagain_rect)
    
    pygame.display.update()
    clock.tick(60)
    