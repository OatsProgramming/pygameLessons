import os, pygame
from sys import exit

os.system('clear')
os.chdir('/Users/jaliljusay/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Jumping and Gravity:

It's hard to replicate actual gravity as it is exponential and that would be cause a lot of stress on the system
For game sakes: actual physics < fun or ease of programming
So we'll do the following:

gravity += some value
player.y += gravity

'''

pygame.init()

screen = pygame.display.set_mode((800, 400))
sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))

# We'll first set up the player's gravity to 0 as it is initially on the ground
player_gravity = 0

text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)

welcome_surface = text_font.render('Welcome to Skyward', False, 'DarkGreen')
welcome_rect = welcome_surface.get_rect(center = (400, 100))

score_surface = text_font.render('Score: ', False, 'DarkGrey')
score_rect = score_surface.get_rect(center = (400, -100))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # We can do the same thing with the mouse
        # mouse pos/collision ---> button press ---> Jump
        # button press ---> mouse pos/collision ---> Jump
        # The latter is much more efficient for this scenario as checking for the mouse's position every frame would be wasteful

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                # This is so that the player can only jump when touching the ground
                player_gravity -= 20
                
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                # Here, we can incorporate the jump by setting the gravity at a negative number
                
                player_gravity -= 20
        if event.type == pygame.KEYUP:
            print("Key has been let go")
        

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(welcome_surface, welcome_rect)
    welcome_rect.y -= 2
    screen.blit(score_surface, score_rect)
    if welcome_rect.bottom <= 0:
        score_rect.y = 100

    screen.blit(snail_surface, snail_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    # This is our player
    # We need to connect the player's gravity with their rectangle
    player_gravity += 0.7
    player_rect.y += player_gravity
    # But in order to incorporate a jump, we need to go at the event loop
    screen.blit(player_surface, player_rect)
    # And since our character will constantly fall down, we need to stop somehow at the ground
    # We will turn off the gravity if it's greater than 300 on the y axis
    if player_rect.bottom >= 300:
        player_gravity = 0
        player_rect.bottom = 300
    
    
    
    if player_rect.colliderect(snail_rect):
        print("Colliding with snail")
   
    
    pygame.display.update()
    clock.tick(60)
    
    
    
