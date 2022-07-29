'''
1) Pygame can help you draw images and play sounds
2) Check for player input (input() stops your code and renders the game useless)
3) Other game dev tools like collisions, creating text, timers, etc

4) Not as good as actual game engines

Why learn Pygame?

1) You solve a lot of problems yourself and become a good programmer in general
2) You can quickly learrn a new game engine or other tools
'''

# Creating a window

import pygame
# The following helps close any code when you call it
from sys import exit

# The initiation of all pygame stuff (Starting the engine)
pygame.init()
width = 800
height = 400
# This will only run once unless you put it in a loop
screen = pygame.display.set_mode((width, height))
# This would change the title
pygame.display.set_caption('Big PP')

'''
Now we gotta figure out how to address framerates and how to keep it consistent at all times
For this exercise, lets try to keep it at 60 fps
60 fps ceiling          Easier to do: tell the computer to pause in btwn frames
60 fps floor            Harder to do: hard to get the computer run faster if its slow in the first place; you need to change the game as well to compensate

'''

# This would help us deal with not only time but as well as the frame rate
# By itself it would do nothing; but in the while loop (look at clock.tick())
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # This to close the window
        if event.type == pygame.QUIT:
            # The following is the polar opposite of pygame.init()
            pygame.quit()
            # This is basically using 'break' for the ENTIRE code
            exit()

    # This will help keep the window open
    # Draws elements
    pygame.display.update()
    # While True, the game should not run faster than 60
    clock.tick(60)

