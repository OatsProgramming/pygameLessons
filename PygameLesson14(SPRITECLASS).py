import pygame, os
from sys import exit
from random import randint, choice

os.system('clear')
os.chdir('/Users/jaliljusay/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Creating Sprite Classes:
So far, we only used simple functions and if statements to manage code
Which works for small games but not for larger projects

Sprite Class (OOP):
A class that contains surfaces and rectangles; and it can be drawn and updated easily

We're going to create a sprite class for the player and another for the obstacles

Drawing Sprites:
Sprite classes arent drawn automatically
It also doesnt work with screen.blit()

Logic to creating Drawing Sprites:
Create Sprites ---> Place sprites in group/ groupsingles ---> draw/update all sprites in that group

Pygame has two kinds of groups:
Group ---> A group of multiple sprites (flies and snails)
GroupSingles ---> A group with a single sprite (player)

The player and the obstacles need to be in different groups btwn them so that we can check if they collide

'''

pygame.init()

# Creating the GroupSingle sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__() # So we can initiate the sprite class within that class so we can access it
        player_walk1 = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('graphics for tutorial/player pngs/player_walk_2.png').convert_alpha
        self.player_jump = pygame.image.load('graphics for tutorial/player pngs/jump.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2] # The reason why we have self is so we access it outside the init method
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (180, 300))
        self.gravity = 0

    # Now we simply put all the code we had for the player into this class
    # The following will be the event loop for keyboard input
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity -= 20
        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_SPACE and player_rect.bottom == 300:
        #     player_gravity -= 20

    def apply_gravity(self):
        # player_gravity += 1
        # player_rect.y += player_gravity
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = 0
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        #     player_gravity = 0
    
    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    # def player_animation():
    #     global player_surface, player_index
    # 
    #     if player_rect.bottom < 300:
    #         player_surface = player_jump
    #     else:
    #         player_index += 0.1 
    #         if player_index >= len(player_walk):
    #             player_index = 0
    #         player_surface = player_walk[int(player_index)] 
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_frame1 = pygame.image.load('graphics for tutorial/fly png/fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('graphics for tutorial/fly png/fly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210

        else:
            snail_frame1 = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
            snail_frame2 = pygame.image.load('graphics for tutorial/snail png/snail2.png').convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
    
    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    # def obstacle_movement(obstacle_list):
    #     if obstacle_list:
    #         for obstacle_rect in obstacle_list:
    #             obstacle_rect.x -= 5
    # 
    #             if obstacle_rect.bottom == 300:
    #                 screen.blit(snail_surface, obstacle_rect)
    #             
    #             else:
    #                 screen.blit(fly_surface, obstacle_rect)
    #         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > 0]
    #         
    #         return obstacle_list
    #     else:
    #         return []

start_time = 0
def getScore():
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score = text_font.render(f"Score: {current_time}", False, "DarkGrey")
    score_rect = score.get_rect(center = (400, 70))
    screen.blit(score, score_rect)
    return current_time


# def obstacle_collision(player, obstacles):
    # if obstacles:
    #     for obstacle_rect in obstacles:
    #         if player.colliderect(obstacle_rect):
    #             return False
    # return True

def collision_sprite():
    # Similar to collision function
    if pygame.sprite.spritecollide(player.sprite, obstacleGroup, False): # If true, snail will be deleted if False snail will not be deleted
        obstacleGroup.empty()
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


# snail_frame1 = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
# snail_frame2 = pygame.image.load('graphics for tutorial/snail png/snail2.png').convert_alpha()
# snail_list = [snail_frame1, snail_frame2]
# snail_index = 0
# snail_surface = snail_list[snail_index]
# 
# fly_frame1 = pygame.image.load('graphics for tutorial/fly png/fly1.png').convert_alpha()
# fly_frame2 = pygame.image.load('graphics for tutorial/fly png/fly2.png').convert_alpha()
# fly_list = [fly_frame1, fly_frame2]
# fly_index = 0
# fly_surface = fly_list[fly_index]

# obstacle_list = []

# Creating a sprite class
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacleGroup = pygame.sprite.Group()

# player_gravity = 0
# player_walk1 = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
# player_walk2 = pygame.image.load('graphics for tutorial/player pngs/player_walk_2.png')
# player_jump = pygame.image.load('graphics for tutorial/player pngs/jump.png')
# player_walk = [player_walk1, player_walk2]
# player_index = 0
# player_surface = player_walk[player_index]
# player_rect = player_surface.get_rect(midbottom = (100, 300))

player_stand = pygame.image.load('graphics for tutorial/player pngs/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


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
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos):
            #         player_gravity -= 20
            
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE and player_rect.bottom == 300:
            #         player_gravity -= 20
            
            if event.type == obstacle_timer:
                obstacleGroup.add(Obstacle(choice['fly', 'snail', 'snail']))
                # if randint(0,2):
                #     obstacle_list.append(snail_surface.get_rect(bottomleft = (randint(800, 1000), 300)))
                # else:
                #     obstacle_list.append(fly_surface.get_rect(bottomleft = (randint(800, 1000), 210)))
        
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
        
        # player_animation()
        # screen.blit(player_surface, player_rect)
        # player_gravity += 1
        # player_rect.y += player_gravity

        # Sprites have two main functions
        player.draw(screen) # To draw
        player.update() # To update'

        obstacleGroup.draw(screen)
        obstacleGroup.update()


        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        #     player_gravity = 0

        # if event.type == snail_animation_timer:
        #     if snail_index == 0:
        #         snail_index = 1
        #     else:
        #         snail_index = 0
        #     snail_surface = snail_list[snail_index]
        # 
        # if event.type == fly_animation_timer:
        #     if fly_index == 0:
        #         fly_index = 1
        #     else:
        #         fly_index = 0
        #     fly_surface = fly_list[fly_index]
        # 
        # obstacle_list = obstacle_movement(obstacle_list)
        game_active = collision_sprite()
    
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

        # obstacle_list.clear()
        # player_rect.midbottom = (100, 300)
        player_gravity = 0

    pygame.display.update()
    clock.tick(60)        
