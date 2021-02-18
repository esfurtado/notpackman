# The following code is based on example.py code to create a simple game.

import pygame
import random

pygame.init()

screen_width = 1100
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))

player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

# Here I am updating the size of the images so they fit better the screen
player = pygame.transform.scale(player, (100, 100))
enemy1 = pygame.transform.scale(enemy1, (100, 100))
enemy2 = pygame.transform.scale(enemy2, (100, 100))
enemy3 = pygame.transform.scale(enemy3, (100, 100))
prize = pygame.transform.scale(prize, (100, 100))

player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()


playerXPosition = 100
playerYPosition = 50

# The following positions have been defined so that the enmemies and prize show at different points of the screen

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition = 900
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
enemy3XPosition = 700
enemy3YPosition = random.randint(0, screen_height - enemy3_height)
prizeXPosition = screen_width - prize_width
prizeYPosition = random.randint(0, screen_height - prize_height)

keyUp = False
keyDown = False
keyleft = False
keyright = False

while 1:

    screen.fill(0) # Clears the screen. (note kept from example)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()# This updates the screen. (note kept from example)
    
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. (note kept from example)
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. (note kept from example)
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT: #pygame.K_RIGHT and K_LEFT allow the use of right and left key pressing commands
                keyright = True
            if event.key == pygame.K_LEFT:
                keyleft = True
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyright = False
            if event.key == pygame.K_LEFT:
                keyleft = False

    if keyUp == True:
         if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
         if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyleft == True:
        if playerXPosition > 0:  #This makes sure the user does not move the player out of screen to the left
            playerXPosition -=1
    if keyright == True:      
        if playerXPosition < screen_width - player_width:  #This makes sure the player does not move out of screen to the right
            playerXPosition +=1

# Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

     # Bounding boxes for the enemies and prize:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        print("You lose!")
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):
        print("You win!")

        pygame.quit()
        
        exit(0)
    
    # This updates the positions of the enemies and prize so they all move at different speeds
    enemy1XPosition -= 0.15
    enemy1YPosition += 0.10
    enemy2XPosition -= 0.12
    enemy2YPosition -= 0.15
    enemy3XPosition -= 0.20
    prizeXPosition -= 0.1

