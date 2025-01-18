import pygame
import random

pygame.init()

# Set up the display
screen_width, screen_height = 1900, 1000
background_url = "forest.jpg"
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interactive Story")

def change_background(url):
        background_image = pygame.image.load(url)
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0,0))

# Set up fonts
font = pygame.font.Font(None, 36)


# Colors
WHITE = (10,0,0)
PURPLE = (39, 1, 74)
GREEN = (32, 140, 93)
MAROON = (102, 41, 55)
RED = (255, 0, 59)
WHITE = (255, 255, 255)
CURRENT_TEXT_COLOR = WHITE


# Story state
scene = 1
wallet = 10

def render_text(lines, COLOUR):
    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, COLOUR)
        screen.blit(text_surface, (277, 50 + y_offset))
        y_offset += font.get_linesize()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scene = 1
                background_url = "forest.jpg"
            elif event.key == pygame.K_2:
                scene = 2
                background_url = "castle.jpg"
            elif event.key == pygame.K_3:
                scene = 3
                background_url = "amg.jpg"
            elif event.key == pygame.K_4:
                scene = 4
                background_url = "amg2.jpg"
            elif event.key == pygame.K_5:
                scene = 5
                background_url = "amg3.jpg"
            elif event.key == pygame.K_6:
                scene = 6
                background_url = "city.jpg"
            elif event.key == pygame.K_7:
                scene = 7
            elif event.key == pygame.K_8:
                scene = 8
            elif event.key == pygame.K_9:
                scene = 9
            elif event.key == pygame.K_b:
                scene = 23
            elif event.key == pygame.K_0:
                scene = 10
            elif event.key == pygame.K_r:
                scene = 1
                background_url = "forest.jpg"
            elif event.key == pygame.K_m:
                scene = 45
            elif event.key == pygame.K_e:
                restaurants = ["restrunt1.jpg", "maccas.jpg" ,"restrunt3.jpg"]
                background_url = restaurants[random.randint(0, 2)]
                scene = 60
            elif event.key == pygame.K_g:
                restaurants = ["pasta.jpg", "food1.jpg" ,"food2.jpg", "food3.jpg"]
                background_url = restaurants[random.randint(0, 3)]
                scene = 565
            elif event.key == pygame.K_f:
                background_url = "thank.png"
                scene = 11


        change_background(background_url)

    # Render text based on the scene
    if scene == 1:
        CURRENT_TEXT_COLOR = GREEN
        lines = [
              "You are in a dark forest.",
              "",
              "Press 2 to go to the castle ."
            ]
    if scene == 2:
        CURRENT_TEXT_COLOR = WHITE
        lines = [
              "you are now in the castle.",
              "",
              "Press 3 to go to the car or  .",
              "  .",
              "Press r to restart the game  ."
            ]
    if scene == 3:
        CURRENT_TEXT_COLOR = WHITE
        lines = [
              "you are now at the car",
              "",
              "Press 4 to enter the car",
              "  .",
              "Press r to restart the game  ."
        ]
    if scene == 4:
       CURRENT_TEXT_COLOR = WHITE
       lines = ["where do you want to drive to ",
                "press r to reset or ",
                "press 5 to get out of the car"
        ]
    if scene == 5:
       CURRENT_TEXT_COLOR = WHITE
       lines = ["you have exited the car",
                "press r to reset or ",
                "press 6 to go to the city"
        ]
    if scene == 6:
       CURRENT_TEXT_COLOR = WHITE
       lines = ["you are now in the city",
                "press r to reset or ",
                "press e to eat"
        ]
    if scene == 60:
       CURRENT_TEXT_COLOR = WHITE
       lines = ["you are now in mistery restrunt 1 ",
                "press r to reset or ",
                "press g to choose a random dish  "
        ]
    
    if scene == 565:
       CURRENT_TEXT_COLOR = WHITE
       lines = ["you are now eating ?",
                "press r to reset or ",
                "press f to finish the game "
        ]
    if scene == 11:
       CURRENT_TEXT_COLOR = WHITE
       lines = [""]
      
       
    render_text(lines, CURRENT_TEXT_COLOR)
    # Update the display
    pygame.display.flip()
    

pygame.quit()


