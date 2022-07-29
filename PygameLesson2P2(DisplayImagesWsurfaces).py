import os, pygame
from sys import exit

os.system('clear')

os.chdir('/Users/username/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial/')
print(os.getcwd())
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Skyward')

# Here, we'll be importing an image instead of using a plain color
# After changing the directory, it should be easy to call out. It's the same as unpickling or opening a file via code.

sky_surface = pygame.image.load('graphics for tutorial/Sky.png')
ground_surface = pygame.image.load('graphics for tutorial/Ground.png')

# After dealing with the images, let's try creating some text
'''
Creating text:

1) create a font (text size and style)
2) write text on a surface
3) blit the text surface
'''
# We're gonna use the font that we have downloaded but we can use the default by typing 'None'
font_type = 'font for tutorial/Pixeltype.ttf'
font_size = 50
test_font = pygame.font.Font(font_type, font_size)
text_info = 'My game'
antialias = False # This is to make the text look more rough rather than smooth
color = 'DarkGreen'
text_surface = test_font.render(text_info, antialias, color)
# Now, blit the text surface


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350,50))

    pygame.display.update()
    clock.tick(60)
