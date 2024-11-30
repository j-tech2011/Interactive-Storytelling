import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((1900,1000))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 36)


# Colors
WHITE = (10,0,0)
BLACK = (237, 9, 9)

# Story state
scene = 1
wallet = 10

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scene = 1
            elif event.key == pygame.K_2:
                    scene = 2
            elif event.key == pygame.K_3:
                    scene = 3
            elif event.key == pygame.K_4:
                    scene = 4
            elif event.key == pygame.K_5:
                    scene = 5
            elif event.key == pygame.K_6:
                    scene = 6
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
            
            

    # Fill the screen with white
    screen.fill(WHITE)

    # Render text based on the scene
    if scene == 1:
        text = font.render("You are in a dark forest. Press 2 to go to the castle.", True, BLACK)
    elif scene == 2:
        text = font.render("You are now in the castle. Press 1 to go back to the forest. press key 3 to go to the car", True, BLACK)
    elif scene == 3:
        text = font.render("you are now in the car press key 4 to get a AK 47 ", True, BLACK)
    elif scene == 4:
        text = font.render("give me 100,000 rubies for the AK 47 press 5 to get your wepon  ", True, BLACK)
    elif scene == 5:
        text = font.render("ok you lost 1,0000000 rubies press 6 to get revenge  ", True, BLACK)
    elif scene == 6:
        text = font.render("you got scammed litttle boi press 7 to punch the scammer  ", True, BLACK)
    elif scene == 7:
        text = font.render("bang you hit the scammer he is out cold run away quickly press 8 to runaway  ", True, BLACK)
    elif scene == 8:
        text = font.render("you got cought u are now in jail WAMP WAMP  ", True, BLACK)
    elif scene == 9:
        text = font.render("GIVE ME MONEY TO GET OUT OF JAIL   ", True, BLACK)
    elif scene == 23:
        text = font.render("bank balance ¥" + str(wallet), True, BLACK)
    elif scene == 10:
        text = font.render( "you do not have enough money brokie you at lest need 100,ooo yen", True, BLACK)
    
    screen.blit(text, (50, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()
