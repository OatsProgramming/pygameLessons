import pygame, os
from sys import exit
from random import randint

os.system('clear')
os.chdir('/Users/username/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Animating the Player, Snail, Fly:
Pretty straightforward concept

We just have to update the surface every couple millisecond

Player animation ---> Create our own timer that updates the surface
Obstacle animation ---> Rely on the inbuild timer to update all obstacle surfaces
'''

pygame.init()

start_time = 0
def getScore():
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score = text_font.render(f"Score: {current_time}", False, "DarkGrey")
    score_rect = score.get_rect(center = (400, 70))
    screen.blit(score, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            
            else:
                screen.blit(fly_surface, obstacle_rect)
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

def player_animation():
    # walk animation if player on floor or display jump animation if player not on floor
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1 # This is to make sure the player walks, not run
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)] # Got to use int to get the whole number of the index


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


# Import obstacle frames and do the same thing
snail_frame1 = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('graphics for tutorial/snail png/snail2.png').convert_alpha()
snail_list = [snail_frame1, snail_frame2]
snail_index = 0
snail_surface = snail_list[snail_index]

fly_frame1 = pygame.image.load('graphics for tutorial/fly png/fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics for tutorial/fly png/fly2.png').convert_alpha()
fly_list = [fly_frame1, fly_frame2]
fly_index = 0
fly_surface = fly_list[fly_index]

obstacle_list = []

player_gravity = 0
# Import the other images for animation
player_walk1 = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics for tutorial/player pngs/player_walk_2.png')
player_jump = pygame.image.load('graphics for tutorial/player pngs/jump.png')
# Create a list of animation to choose
player_walk = [player_walk1, player_walk2]
player_index = 0
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (100, 300))

player_stand = pygame.image.load('graphics for tutorial/player pngs/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


# Below are obstacle timers
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 800)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 300)

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
            
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_list.append(snail_surface.get_rect(bottomleft = (randint(800, 1000), 300)))
                else:
                    obstacle_list.append(fly_surface.get_rect(bottomleft = (randint(800, 1000), 210)))
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = pygame.time.get_ticks() // 1000
                game_active = True        
    
    if game_active:

        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(welcome_surface, welcome_rect)
        welcome_rect.y -= 2
        if welcome_rect.bottom <= 0:
            score = getScore()
        
        player_animation()
        screen.blit(player_surface, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0

        # Below are to constantly change the index for the obstacles
        if event.type == snail_animation_timer:
            if snail_index == 0:
                snail_index = 1
            else:
                snail_index = 0
            snail_surface = snail_list[snail_index]
        
        if event.type == fly_animation_timer:
            if fly_index == 0:
                fly_index = 1
            else:
                fly_index = 0
            fly_surface = fly_list[fly_index]
        
        obstacle_list = obstacle_movement(obstacle_list)
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

        obstacle_list.clear()
        player_rect.midbottom = (100, 300)
        player_gravity = 0

    pygame.display.update()
    clock.tick(60)        
