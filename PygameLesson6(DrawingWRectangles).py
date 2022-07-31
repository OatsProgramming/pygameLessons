import os, pygame
from sys import exit

os.system('clear')
os.chdir('/Users/jaliljusay/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial')

'''
pygame.draw:

draw rectangles, circles, lines, ellipses, etc.

pygame.draw."insert shape"
Shapes:

rect
polygon
circle
ellipse
arc
line
lines
aaline
aalines


colors:
RGB v Hexadecimal
RGB = red + green + blue (intuitive)

rgb_color = (red, green, blue)
rgb_color lowest to highest values: 0 - 255

hex_color = #rrggbb
hex_color lowest to highest values 00 - ff

Just use photoshop or some color thing thatll give you the numbers
'''

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Welcome to Skyward')

sky_surface = pygame.image.load('graphics for tutorial/sky.png').convert()
ground_surface = pygame.image.load('graphics for tutorial/ground.png').convert()

snail_surface = pygame.image.load('graphics for tutorial/snail png/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

player_surface = pygame.image.load('graphics for tutorial/player pngs/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))

text_font = pygame.font.Font('font for tutorial/Pixeltype.ttf', 50)
text_surface = text_font.render('Welcome to Skyward', False, 'DarkGreen')
text_rect = text_surface.get_rect(center = (400, 200))

# We'll do a RGB color
score_surf = text_font.render('Score: ', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')
        

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, text_rect)
    text_rect.y -= 1
    score_rect.bottom = 0
    if text_rect.y <= 0:
        score_rect.y = 50


    # pygame.draw."insert shape"(surface, color, choose object rectangle, width, edge smoothness)
    # We'll use hexidecimal color
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    # This is to draw a line across the screen
    #   pygame.draw.line(screen, 'gold', (0, 0), (800, 400), 10)
    # This is to draw a line that follows the mouse
    #   pygame.draw.line(screen, 'gold', (0,0), pygame.mouse.get_pos(), 10)
    # This to draw an ellipse
    #   pygame.draw.ellipse(screen, 'brown', pygame.Rect(50, 200, 100, 100))



    screen.blit(score_surf, score_rect)
   
    screen.blit(snail_surface, snail_rect)
    snail_rect.x -= 2
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(player_surface, player_rect)




    # mouse = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse):
    #     player_rect.y += 2
    if player_rect.colliderect(snail_rect):
        player_rect.y -= 2
    
    pygame.display.update()
    clock.tick(60)

