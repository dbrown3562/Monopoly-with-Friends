import pygame
import os
import sys
import random

import boardscreen
import popup

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#----------------Helper Functions------------------#
#Def calculate rent
def calcRent(board, players, curPlayerPos, dice1, dice2):
    property = board[curPlayerPos]
    if property.owner != 9:
        player = players[property.owner-1]

    if property.set != "Train" and property.set != "Utility" and property.set != "Tax":
        rentOwed = property.rents[property.houses]
        if property.set in player.monopolies and property.houses == 0:
            rentOwed *= 2

    elif property.set == "Train":
        trainCount = 0
        i = 5
        while i < len(player.properties):
            if player.properties[i] != None:
                trainCount+=1
            i+=10
        rentOwed = property.rents[trainCount]

    elif property.set == "Utility":
        if property.set in player.monopolies:
            rentOwed = (dice1+dice2) * property.rents[1]
        else:
            rentOwed = (dice1+dice2) * property.rents[0]
    
    elif property.set == "Tax":
        rentOwed = property.rents[0]
    
    return rentOwed


#Roll dice... done :)
def clickRoll(players, board, curPlayer, rolled, dice1, dice2, doubles, popUp, screen, sprites):
#Pay to leave popup..
    if curPlayer.jail == True:
        curPlayer.jailCount += 1
    curTime = pygame.time.get_ticks()
    #Roll dice animation
    while pygame.time.get_ticks() < curTime + 1000:
        boardscreen.drawBoard(screen, board, players, sprites)
        boardscreen.drawPlayers(players, screen, sprites)
        boardscreen.drawUI(screen, players, rolled, board, curPlayer, sprites, status = 1)
        boardscreen.rollDiceAnimation(screen, sprites)
        pygame.time.wait(10)
        pygame.display.update()

    rolled = True
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1==dice2:
        doubles += 1
        rolled = False
        if curPlayer.jail == True:
            curPlayer.jail = False
            curPlayer.jailCount = 0
            rolled = True

    if curPlayer.jailCount == 3:
        curPlayer.money -= 50
        curPlayer.jailCount = 0
        curPlayer.jail = False

    if doubles < 3 and curPlayer.jail == False:
        movePlayer(curPlayer, dice1 + dice2)
        #Player lands on an unexplored board piece
        if board[curPlayer.position].owner == 0:
            popUp = "Buy"
        elif board[curPlayer.position].owner != curPlayer.id:
            if board[curPlayer.position].owner == 9 and board[curPlayer.position].set == "Tax":
                popUp = "Rent"
            elif board[curPlayer.position].owner != 9:
                popUp = "Rent"
    else:
        doubles = 0
        curPlayer.position = 10
        rolled = True
        curPlayer.jail = True

    #Wait/Animate Player movement
    curTime = pygame.time.get_ticks()
    while pygame.time.get_ticks() < curTime + 1000:
        boardscreen.drawBoard(screen, board, players, sprites)
        boardscreen.drawPlayers(players, screen, sprites)
        boardscreen.drawUI(screen, players, rolled, board, curPlayer, sprites, status = 1)
        boardscreen.drawDice(dice1, dice2, screen, sprites)
        pygame.display.update()
    
    return rolled, curPlayer, dice1, dice2, popUp, doubles


def payRent(board, players, curPlayer, dice1, dice2):
    rentOwed = calcRent(board, players, curPlayer.position, dice1, dice2)
    curPlayer.money -= rentOwed
    if board[curPlayer.position].owner != 9:
        players[board[curPlayer.position].owner - 1].money += rentOwed


#Main Game Engine, handles movement and whatnot. Needs access to a screen.
def movePlayer(player, distance):
    player.position += distance
    if(player.position >= 40):
        player.position -= 40
        player.money += 200
    if(player.position == 30):
        player.position = 10
        player.jail = True

#Resolves all click events
def resolve(mouseX, mouseY, board, players, popUp, rolled, curPlayer, doubles, dice1, dice2, screen, sprites):
#Player has clicked roll
    if(mouseX >= 910 and mouseX <= 1010):
        if(mouseY >= 950 and mouseY <= 1000):
            if(not rolled and popUp == "None"):
                rolled, curPlayer, dice1, dice2, popUp, doubles = clickRoll(players, board, curPlayer, rolled, dice1, dice2, doubles, popUp, screen, sprites)
        #Player has clicked end turn
        if(mouseY >= 1010 and mouseY <= 1060 and rolled == True and popUp == "None"):
            doubles = 0
            rolled = False
            players[curPlayer.id-1] = curPlayer #Save the player's state
            if curPlayer.id == len(players):
                curPlayer = players[0]
            else:
                curPlayer = players[curPlayer.id]
    
    #Player is currently in a buy popup menu
    if popUp == "Buy":
        if mouseY >= 700 and mouseY <= 750: #In the right Y coordinates
            if mouseX >= 810 and mouseX <= 910: #Yes
                popUp = "None"
                if curPlayer.money - board[curPlayer.position].price > 0:
                    curPlayer.money -= board[curPlayer.position].price
                    board[curPlayer.position].owner = curPlayer.id
                    players[curPlayer.id-1].properties[curPlayer.position] = board[curPlayer.position]
                #Tell the user to mortgage or some crap idk
                else:
                    pass
            elif mouseX >= 1010 and mouseX <= 1110: #No
                popUp = "None"
    
    if popUp == "Rent":
        if mouseY >= 700 and mouseY <= 750: #In the right Y coordinates
            if mouseX >= 910 and mouseX <= 1010: #Pay
                payRent(board, players, curPlayer, dice1, dice2)
                popUp = "None"
                

    return popUp, rolled, curPlayer, doubles, dice1, dice2


def init():
    pygame.init()
    #Get all of the sprites
    sprites = dict()
    directory = resource_path('assets')

    for filename in os.scandir(directory):
        imgURL = resource_path('assets\\' + filename.name)
        img = pygame.image.load(imgURL)#
        sprites[filename.name] = img
    
    return sprites