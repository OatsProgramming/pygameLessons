import os, pygame
from random import choice, randint
from sys import exit

os.system('clear')
os.chdir('/Users/jaliljusay/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
Note to SELF about SPRITE CLASSES:
To draw, ALWAYS ALWAYS ALWAYSSSSSSSS use self.image and self.rect ALWAYS
'''

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load up the images for animation
        player_walk1 = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha() # Convert it to improve runtime
        player_walk2 = pygame.image.load('graphics for tutorial/player pngs/player_walk_2.png').convert_alpha() # Same for the rest of the imported images
        self.player_jump = pygame.image.load('graphics for tutorial/player pngs/jump.png').convert_alpha()
        # Put the images into a list
        self.frames = [player_walk1, player_walk2]
        # Setting the default to index 0
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_rect(midbottom = (100, 300))
        self.gravity = 0

        # Load jump sfx
        self.jump_sound = pygame.mixer.Sound('audio for tutorial/jump.mp3')
        self.jump_sound.set_volume(0.5) # Self explanatory

    def apply_gravity (self):
        # Continuously apply gravity on the player's y axis
        self.rect.y += self.gravity
        if self.rect.bottom <= 300:
            self.gravity += 1
        # Unless the player is on the ground
        else:
            self.rect.bottom = 300
            self.gravity = 0

    def player_input(self):
        # If the space button is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            # Make the player jump
            self.gravity -= 20
            self.jump_sound.play() 
    
    def animation(self):
        if self.rect.bottom == 300: 
            self.frames_index += 0.1
            if self.frames_index > len(self.frames):
                self.frames_index = 0
            self.image = self.frames[int(self.frames_index)]
        else:
            self.image = self.player_jump
        
        
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        # Depending on choice, either will load fly or snail for better runtime
        if type == 'fly':
            fly_1 = pygame.image.load('graphics for tutorial/fly png/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics for tutorial/fly png/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        
        elif type == 'snail':
            snail_1 = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics for tutorial/snail png/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300


        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        # x position will be randomly selected btwn 800 - 1000 pixels
        self.rect = self.image.get_rect(bottomleft = (randint(800,1000), y_pos))

    def animation(self):
        self.frames_index += 0.1
        if self.frames_index > len(self.frames):
            self.frames_index = 0
        self.image = self.frames[int(self.frames_index)]
    
    def destroy(self):
        # Delete the obstacle when it reaches outside of the screen
        if self.rect.right < 0:
            self.kill()
    
    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()


def get_score():
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score_surf = text_font.render(f'Score: {current_time}', False, 'DarkGrey')
    score_rect = score_surf.get_rect(center = (400, 100))
    screen.blit(score_surf, score_rect)
    # This will be useful later as it will display the end score at the end of the game
    return current_time 

def collision():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        # game_active = False
        return False
    else:
        # game_active = True
        return True

pygame.init() # Initiate pygame

# Defaults
game_active = False
start_time = 0
score = 0

# Set up
text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Skyward')

# Load Background Music
bg_music = pygame.mixer.Sound('audio for tutorial/music.wav')
bg_music.play(loops = -1) # Loop BG

# For fps
clock = pygame.time.Clock()


# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Create the intro scene
player_stand = pygame.image.load('graphics for tutorial/player pngs/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

title_surf = text_font.render('Skyward', False, 'Black')
title_surf = pygame.transform.scale2x(title_surf)
title_rect = title_surf.get_rect(center = (400, 70))

start_surf = text_font.render('Press Space to start', False, 'black')
start_rect = start_surf.get_rect(center = (400, 350))

# Main stuff when game starts
sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

# Create timer for obstacles
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) # Every 1.5 seconds an obstacle will spawn

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Will exit the game and fully shut down the program
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacles(choice(['fly', 'snail', 'snail'])))
        
        else:
            # If user dies and wants to continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                # Reset score
                start_time = pygame.time.get_ticks() // 1000

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        score = get_score() # This will help display the score

        player.draw(screen) # This will initiate the Player Sprite Class
        player.update() # This will constantly update it

        obstacle_group.draw(screen) # Initiates the obstacle Sprite Class
        obstacle_group.update() # updates it

        game_active = collision() # Checks to see if theres a collision. Will return False if there is one, resulting in game over screen
    
    # Game over screen
    else:
        screen.fill('#437E7B')
        screen.blit(player_stand, player_stand_rect)
        score_message = text_font.render(f"Final Score: {score}", False, 'Black')
        score_message = pygame.transform.scale2x(score_message)
        score_rect = score_message.get_rect(center = (400, 70))
        play_again = text_font.render('Press Space to play again', True, 'Black')
        play_rect = play_again.get_rect(center = (400, 350))
        screen.blit(play_again, play_rect)
        screen.blit(score_message, score_rect)

        # Starting screen
        if score == 0:
            screen.fill('#437E7B')
            screen.blit(player_stand, player_stand_rect)
            screen.blit(title_surf, title_rect)
            screen.blit(start_surf, start_rect)

    # To constantly update the screen    
    pygame.display.update()
    # To set the fps
    clock.tick(60)
    

