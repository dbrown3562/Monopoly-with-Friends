from asyncio.windows_events import NULL
import pygame
import os
import sys
import random

import engine

#This some bs for pyinstaller to work.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pygame.font.init()
font = pygame.font.Font(resource_path('fonts\\calibri.ttf'), 20)
font.bold = True

#Helper functions
def drawBox(screen, sprites):
    #Create a semi-black overlay
    tint = pygame.Surface((1920,1080), pygame.FULLSCREEN)
    tint.set_alpha(128)
    tint.fill((0,0,0))
    screen.blit(tint, (0,0))

    #Draw the popup menu
    img = sprites['popup.png']
    screen.blit(img, (760, 580))

def drawProperty(screen, board, curPlayerPos, sprites):
    property = board[curPlayerPos]
    #Draw the property card
    try:
        if property.owner != 9: #Just in case some tomfoolery occurs
            img = sprites[str(curPlayerPos) + 'Card.png']
            screen.blit(img, (810, 250))
    except Exception:
        pass



#Create a popup menu with buttons saying you can buy this property for XYZ
def askToBuy(screen, board, curPlayerPos, sprites):
    property = board[curPlayerPos]
    drawBox(screen, sprites)
    #Draw the necessary text on said window
    txt1 = 'Would you like to purchase'
    txt2 = property.name + ' for M' + str(property.price) + '?'
    text1 = font.render(txt1, True, (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = (960, 640)
    screen.blit(text1, textRect1)
    text2 = font.render(txt2, True, (0,0,0))
    textRect2 = text2.get_rect()
    textRect2.center = (960, 670)
    screen.blit(text2, textRect2)

    #Draw the buttons
    img = sprites['Yes.png']
    screen.blit(img, (810, 700))

    img = sprites['No.png']
    screen.blit(img, (1010, 700))
    drawProperty(screen, board, curPlayerPos, sprites)
    

#Create a popup notifying the user that they owe rent
def rentPopUp(screen, board, curPlayerPos, players, dice1, dice2, sprites):
    drawBox(screen, sprites)

    rentOwed = engine.calcRent(board, players, curPlayerPos, dice1, dice2)

    if board[curPlayerPos].set != "Tax":
        txt1 = 'You owe ' + players[board[curPlayerPos].owner - 1].alias
        txt2 = 'M' + str(rentOwed) + ' in rent!'
    else:
        txt1 = 'You owe the government'
        txt2 = 'M' + str(rentOwed) + ' in taxes!'

    text1 = font.render(txt1, True, (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = (960, 640)
    screen.blit(text1, textRect1)
    text2 = font.render(txt2, True, (0,0,0))
    textRect2 = text2.get_rect()
    textRect2.center = (960, 670)
    screen.blit(text2, textRect2)

    #Draw the buttons
    img = sprites['Pay.png']
    screen.blit(img, (910, 700))

    drawProperty(screen, board, curPlayerPos, sprites)
