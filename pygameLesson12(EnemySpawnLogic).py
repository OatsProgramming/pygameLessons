import pygame, os
from sys import exit
from random import randint

os.system('clear')
os.chdir('/Users/username/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Spawning enemies:

1) Create a custom event
2) tell pygame to trigger that event continuously
3) add code in event loop

New Obstacle Logic:

1) We create a list of obstacle rectangles 
2) Everytime the timer triggers, we add a new rectangle to that list
3) We move every rectangle in that list to the left of every frame
4) If it goes to far to the left, delete that rectangle

Fixing the Collision logic

After assesing the obstacle rectangles, we need to create a new function 
and itll either return True or False

'''

pygame.init()

start_time = 0
def getScore():
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score = text_font.render(f"Score: {current_time}", False, "DarkGrey")
    score_rect = score.get_rect(center = (400, 70))
    screen.blit(score, score_rect)
    return current_time

# NEW review when Not as sleepy
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            # This is to get the snail to show if the rectangle bottom is 300
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            

            # This is to show the fly if anything else
            else:
                screen.blit(fly_surface, obstacle_rect)
                
        # This is to only copy if obstacle is in screen
        # Ultimately deletes the obstacle if off screen
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > 0]
        
        return obstacle_list
    else:
        return []

def obstacle_collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True



score = 0
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Skyward')

sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)

welcome_surface = text_font.render('Welcome to Skyward', False, "DarkGreen")
welcome_rect = welcome_surface.get_rect(center = (400, 100))

game_name = text_font.render('Skyward', False, "black")
game_name = pygame.transform.scale2x(game_name)
game_rect = game_name.get_rect(center = (400, 70))
game_active = False

playagain = text_font.render('Press Space to play again', False, 'Black')
playagain_rect = playagain.get_rect(center = (400, 325))

# OBSTACLES
snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
# ALSO: We dont need the snail rectangle anymore; its in our STEP 2 OBSTACLE LOGIC
# snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

fly_surface = pygame.image.load('graphics for tutorial/fly png/fly1.png').convert_alpha()

# Create an obstacle list STEP 1 NEW OBSTACLE LOGIC
obstacle_list = []

player_gravity = 0
player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))

player_stand = pygame.image.load('graphics for tutorial/player pngs/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# We'll go ahead and create a new event STEP 1 SPAWNING
obstacle_timer = pygame.USEREVENT 

# STEP 2: The event we want to trigger, and how often we want to trigger in milliseconds
pygame.time.set_timer(obstacle_timer, 1500)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity -= 20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity -= 20
            
            # STEP 3 SPAWNING
            if event.type == obstacle_timer:
                # STEP 2 OBSTACLE LOGIC
                # We have to try and figure out a way to implement both the snail and fly to be randomly selected
                # With the following if statement, it'll either 1 or 0: True or False respectively
                if randint(0,2):
                    obstacle_list.append(snail_surface.get_rect(bottomleft = (randint(800, 1000), 300)))
                else:
                    obstacle_list.append(fly_surface.get_rect(bottomleft = (randint(800, 1000), 210)))
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = pygame.time.get_ticks() // 1000
                game_active = True
                # snail_rect.left = 800
        
    
    if game_active:

        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(welcome_surface, welcome_rect)
        welcome_rect.y -= 2
        if welcome_rect.bottom <= 0:
            score = getScore()
            
        # REMOVING THIS AS ITS NO LONGER NEEDED SINCE WE GOT A TIMER NOW
        
        # screen.blit(snail_surface, snail_rect)
        # snail_rect.x -= 3
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800

        screen.blit(player_surface, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0
        
        # Obstacle Movement
        obstacle_list = obstacle_movement(obstacle_list)
        
        # if snail_rect.colliderect(player_rect):
        #     game_active = False

        # This will return True continuously until it collides
        game_active = obstacle_collision(player_rect, obstacle_list)
    
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

        screen.blit(player_stand, player_stand_rect)

        # This is to remove all the items in the list; ultimately restarts the obstacles
        obstacle_list.clear()
        # The following will just restart the players position
        player_rect.midbottom = (100, 300)
        player_gravity = 0

    pygame.display.update()
    clock.tick(60)        
