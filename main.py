#import all of the parameters
from re import M
import pygame
import os
import sys
import random

import player
import engine
import property
import boardscreen
import popup

#Size of the window
MAXWIDTH = 1920
MAXHEIGHT = 1080

dice1 = 1
dice2 = 1

#Gamestates
rolled = False
doubles = 0
popUp = "None"

#Initialize the Game
sprites = engine.init()
pygame.display.set_icon(sprites['monopolyman.png'])
screen = pygame.display.set_mode((MAXWIDTH,MAXHEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Monopoly with Friends")
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()
board = property.generateBoard()

#initialize the players
player1 = player.Player(1,"Player 1",1500,0,[None]*40,(0,100,100))
player2 = player.Player(2,"Cat",1500,0,[None]*40,(100,0,100))
player3 = player.Player(3,"Player 3",1500,0,[None]*40,(100,100,0))
player4 = player.Player(4,"Player 4",1500,0,[None]*40,(0,0,100))
player5 = player.Player(5,"Player 5",1500,0,[None]*40,(0,100,25))
player6 = player.Player(6,"Player 6",1500,0,[None]*40,(50,100,0))
player7 = player.Player(7,"Player 7",1500,0,[None]*40,(100,0,0))
player8 = player.Player(8,"Player 8",1500,0,[None]*40,(50,33,40))

i = 0

#Create the player list (This will be populated based on present connections or smth idk)
players = [player1, player2, player3, player4, player5, player6, player7, player8]
curPlayer = players[0]

#Declare controller inputs
esc_down = False
q_down = False
clicked = False
space_down = False

#Draw the Screen

#Gameplay loop
running = True
while running:
    mouseX, mouseY = pygame.mouse.get_pos()
    #Start the event loop
    for event in pygame.event.get():

        #Handle Keyboard inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                esc_down = True

            #If Q is pressed, quit
            if event.key == pygame.K_q:
                q_down = True

            if event.key == pygame.K_SPACE:
                space_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                esc_down = False

        #Click event. Will be more robust once positioning is introduced.
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = True
            mouseX, mouseY = pygame.mouse.get_pos()

        #Detect if game has been exited
        if event.type == pygame.QUIT:
            running = False

    #Resolve controller events
    if esc_down: 
        if popUp == "Buy":
            popUp = "None"

    if q_down:
        pygame.quit()
        sys.exit()

    if clicked:
        popUp, rolled, curPlayer, doubles, dice1, dice2 = engine.resolve(mouseX, mouseY, board, players, popUp, rolled, curPlayer, doubles, dice1, dice2, screen, sprites)
        clicked = False

    #Draw the stuff
    boardscreen.drawBoard(screen, board, players, sprites)
    boardscreen.drawPlayers(players, screen, sprites)
    boardscreen.drawDice(dice1, dice2, screen, sprites)
    
    #Popups
    if popUp == "None":
        boardscreen.displayProperty(mouseX, mouseY, screen, sprites)
        boardscreen.drawUI(screen, players, rolled, board, curPlayer, sprites)
    if popUp == "Buy":
        boardscreen.drawUI(screen, players, rolled, board, curPlayer, sprites, status = 1)
        popup.askToBuy(screen, board, curPlayer.position, sprites)
    if popUp == "Rent":
        boardscreen.drawUI(screen, players, rolled, board, curPlayer, sprites, status = 1)
        popup.rentPopUp(screen, board, curPlayer.position, players, dice1, dice2, sprites)

    #Necessary screen stuff
    pygame.display.flip()
    screen.fill((10,10,10))
    clock.tick(30)

pygame.quit()