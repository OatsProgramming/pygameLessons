import pygame, os
from sys import exit

os.system('clear')
os.chdir('/Users/jaliljusay/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

pygame.init()

'''
Transforming Surfaces: to scale, rotate, etc

Refer to pygame library for more details

pygame.transform.'insert here'

scale (width, height)
scale2x(Just the surface and make 2x bigger)
rotozoom(can manipulate angle and scale) but theres a filter

Lets also display the score at the end
So we can do either of these
1) We store the score in a function
2) current_time needs to be global or be returned

'''
# Since we're making the game intro, we'll make the game_active equal to False
game_active = False

start_time = 0
score = 0
def getScore():
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score_surface = text_font.render(f"Score: {current_time}", False, "DarkGrey")
    score_rect = score_surface.get_rect(center = (400, 70))
    screen.blit(score_surface, score_rect)
    return current_time

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Skyward')

sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)

welcome_surface = text_font.render('Welcome to Skyward', False, "DarkGreen")
welcome_rect = welcome_surface.get_rect(center = (400, 100))

# Game title we're adding
game_name = text_font.render('Skyward', False, "black")
game_name = pygame.transform.scale2x(game_name)
game_rect = game_name.get_rect(center = (400, 70))

playagain = text_font.render('Press Space to play again', False, 'Black')
playagain_rect = playagain.get_rect(center = (400, 325))


snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

player_gravity = 0
player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))

# Here we can manipulate the size of the image
# We simply load the image and transform it. The rest remains the same
player_stand = pygame.image.load('graphics for tutorial/player pngs/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

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
                snail_rect.left = 800
                start_time = pygame.time.get_ticks() // 1000
                game_active = True
    
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        screen.blit(welcome_surface, welcome_rect)
        welcome_rect.y -= 2
        if welcome_rect.bottom <= 0:
            score = getScore()
        
        screen.blit(snail_surface, snail_rect)
        snail_rect.x -= 3
        if snail_rect.right <= 0:
            snail_rect.left = 800
        
        player_gravity += 1
        screen.blit(player_surface, player_rect)
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_gravity = 0
            player_rect.bottom = 300
        
        if player_rect.colliderect(snail_rect):
            game_active = False

    else:
        screen.fill('#437E7B')

        score_message = text_font.render(f"Score: {score}", False, 'Black')
        score_message = pygame.transform.scale2x(score_message)
        score_rect = score_message.get_rect(center = (400, 75))
        if score == 0:
            screen.blit(game_name, game_rect)
            play = text_font.render('Press Space to play', False, 'Black')
            play_rect = play.get_rect(center = (400, 350))
            screen.blit(play, play_rect)
        else:
            screen.blit(score_message, score_rect)
            screen.blit(playagain, playagain_rect)

        # We'll attach the scaled up image here
        screen.blit(player_stand, player_stand_rect)
    

        
    
    pygame.display.update()
    clock.tick(60)

