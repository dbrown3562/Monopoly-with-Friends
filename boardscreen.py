from asyncio.windows_events import NULL
from audioop import add
from pickle import ADDITEMS
from tkinter.font import BOLD
import pygame
import os
import sys
import random

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

def colorAdder(img, owner, players):
    if owner >=1 and owner <= 8:
        img.fill(players[owner-1].color, special_flags=pygame.BLEND_SUB)

#Properties is now an ordered list of possible properties :)
#Flip is either 1 or -1 and determines how the cards go forward and back
def propertyHelper(Xpos, Ypos, properties, flip, board, screen, sprites):
    i = 1
    x = Xpos
    y = Ypos
    while i < len(properties):
        #For all non utility and station cards
        if properties[i] != None and properties[i].set != "Train" and properties[i].set != "Utility": #This is to say the player currently owns the property :)
            #Draw it based on the starting X and Y positions.
            img = sprites[str(i) + '.png']
            img = pygame.transform.scale(img, (25,30))
            screen.blit(img, (x, y))
        if board[i].owner != 9 and board[i].name != "Electric Company" and board[i].name != "Water Works":
            y+=10
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 36:
            y = Ypos
            x+=flip*30
        i+=1
    i = 5
    
    y = Ypos
    x+=flip*30
    while i < len(properties): #iterate through choo choos
        if properties[i] != None:
            img = sprites[str(i) + '.png'].copy()
            img = pygame.transform.scale(img, (25,30))
            screen.blit(img, (x, y))
            y+=10
        i+=10
    
    y = Ypos
    x+=flip*30
    i=12
    #finally, utilities
    while i < len(properties): #iterate through choo choos
        if properties[i] != None:
            img = sprites[str(i) + '.png'].copy()
            img = pygame.transform.scale(img, (25,30))
            screen.blit(img, (x, y))
            y+=10
        i+=16

def drawBoard(screen, board, players, sprites):
    img = sprites['wood.png'].copy()
    img = pygame.transform.scale(img, (1920,1080))
    screen.blit(img, (0,0))
    
    i = 1
    img = sprites['0.png'].copy()
    screen.blit(img, (1298, 800))
    while i < 10:
        img = sprites[str(i) + '.png'].copy()
        colorAdder(img, board[i].owner, players)
        screen.blit(img, (1223-75*(i-1),(800)))
        i+=1

    img = sprites['10.png'].copy()
    screen.blit(img, (503, 800))

    i = 11
    while i < 20:
        img = sprites[str(i) + '.png'].copy()
        img = pygame.transform.rotate(img, 270)
        colorAdder(img, board[i].owner, players)
        screen.blit(img, (503,(800-(i-10)*75)))
        i+=1


    img = sprites['20.png'].copy()
    img = pygame.transform.rotate(img, 270)
    screen.blit(img, (503, 5))

    i = 21
    while i < 30:
        img = sprites[str(i) + '.png'].copy()
        img = pygame.transform.rotate(img, 180)
        colorAdder(img, board[i].owner, players)
        screen.blit(img, (548 + (i-20)*75,(5)))
        i+=1
    
    img = sprites['30.png'].copy()
    img = pygame.transform.rotate(img, 180)
    screen.blit(img, (1298, 5))

    i = 31
    while i < 40:
        img = sprites[str(i) + '.png'].copy()
        img = pygame.transform.rotate(img, 90)
        colorAdder(img, board[i].owner, players)
        screen.blit(img, (1298,(125+(i-31)*75)))
        i+=1

    img = sprites['Back.png'].copy()
    screen.blit(img, (623, 125))
    

#Draw all of the players on the board
def drawPlayers(players, screen, sprites):
    for i in players:
        img = sprites['P1.png'].copy()
        colorAdder(img, i.id, players)
        # if i.position == 0:
        #     screen.blit(img, (1260 + i.id*8,(900)))
        j = 0
        while j < 40:
            if i.position == j:
                if j == 0:
                    screen.blit(img, (1310 + i.id*8,(850)))
                if j == 10:
                    if i.id < 5 and i.jail == False:
                        screen.blit(img, (503,(823 + i.id*8)))
                    elif i.jail == False:
                        screen.blit(img, (535 + (i.id-4)*8,(893)))
                    elif i.id < 5 and i.jail == True:
                        screen.blit(img, (565 + (i.id-4)*8,(813)))
                    else:
                        screen.blit(img, (565 + (i.id-8)*8,(838)))
                if j == 20:
                    screen.blit(img, (515 + i.id*8,(50)))
                if j == 30:
                    screen.blit(img, (1340,(50)))

                if j < 10 and j != 0:
                    if i.id < 5:
                        screen.blit(img, (1230 + i.id*8 - 75*(j-1),(850)))
                    else:
                        screen.blit(img, (1230 + (i.id-4)*8 - 75*(j-1),(875)))
                
                if j < 20 and j > 10:
                    if i.id < 5:
                        screen.blit(img, (548,(800-75*(j-10)+ i.id*8)))
                    else:
                        screen.blit(img, (523,(800-75*(j-10)+ (i.id-4)*8)))

                if j < 30 and j > 20:
                    if i.id < 5:
                        screen.blit(img, (630 + i.id*8 + 75*(j-21),(50)))
                    else:
                        screen.blit(img, (630 + (i.id-4)*8 + 75*(j-21),(25)))

                if j < 40 and j > 30:
                    if i.id < 5:
                        screen.blit(img, (1350,(55+75*(j-30)+ i.id*8)))
                    else:
                        screen.blit(img, (1375,(55+75*(j-30)+ (i.id-4)*8)))
            
            j+=1

#Draw the buttons and players :)
#Status is gonna be smth neat. 0 is nothing, 1 is block all buttons
def drawUI(screen, players, rolled, board, curPlayer, sprites, status = 0):
    #Current Player's Turn message
    txt1 = curPlayer.alias + '\'s Turn'
    text1 = font.render(txt1, True, (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = (960, 940)
    screen.blit(text1, textRect1)

    #Roll Button
    img = sprites['RollButton.png'].copy()

    if(rolled or status == 1):
        img.fill((120,120,120), special_flags=pygame.BLEND_SUB)
    screen.blit(img, (910, 950))

    #End Button
    img = sprites['EndTurnButton.png'].copy()

    if((not rolled) or status == 1):
        img.fill((120,120,120), special_flags=pygame.BLEND_SUB)
    screen.blit(img, (910, 1010))

    #Mortgage Button
    img = sprites['Mortgage.png'].copy()
    if(0):
        img.fill((120,120,120), special_flags=pygame.BLEND_SUB)
    screen.blit(img, (1120, 985))

    #Build Button
    img = sprites['Houses.png'].copy()
    if(0):
        img.fill((120,120,120), special_flags=pygame.BLEND_SUB)
    screen.blit(img, (700, 985))

    #Trade Button
    img = sprites['Trade.png'].copy()
    if(0):
        img.fill((120,120,120), special_flags=pygame.BLEND_SUB)
    screen.blit(img, (550, 985))

    #Quit Button
    img = img = sprites['Bankrupt.png'].copy()
    if(0):
        img.fill((120,120,120), special_flags=pygame.BLEND_SUB)
    screen.blit(img, (1270, 985))



    #Players
    j = 0
    for i in players:
        #Draw the circle
        img1 = img = sprites['Icon.png'].copy()
        img1.fill(i.color, special_flags=pygame.BLEND_SUB)
        img2 = img = sprites['Ring.png'].copy()
        img3 = img = sprites['Line.png'].copy()
        img4 =img = sprites['JailOverlay.png'].copy()

        #Draw the circle n stuff.
        if i.id % 2 == 1:
            #Icon and Line
            screen.blit(img3, (110, 25+300*j))
            screen.blit(img1, (5, 5+300*j))
            screen.blit(img2, (5, 5+300*j)) 
            if i.jail:
               screen.blit(img4, (5, 5+300*j))  

            #Character art here

            #Name and Money
            text = font.render(i.alias, True, (0,0,0))
            textRect = text.get_rect()
            textRect.left = 130
            textRect.top = 30+300*j
            screen.blit(text, textRect)

            text = font.render('M'+ str(i.money), True, (0,0,0))
            textRect = text.get_rect()
            textRect.left = 320
            textRect.top = 30+300*j
            screen.blit(text, textRect)

            #Properties
            propertyHelper(135, 60+300*j,i.properties,1,board,screen, sprites)
        else:
            img3 = pygame.transform.flip(img3, True, False)
            screen.blit(img3, (1485, 25+300*j))
            screen.blit(img1, (1790, 5+300*j))
            screen.blit(img2, (1790, 5+300*j))
            if i.jail:
               screen.blit(img4, (1790, 5+300*j))  

            #Name and Money
            text = font.render(i.alias, True, (0,0,0))
            textRect = text.get_rect()
            textRect.right = 1785
            textRect.top = 30+300*j
            screen.blit(text, textRect)

            text = font.render('M'+ str(i.money), True, (0,0,0))
            textRect = text.get_rect()
            textRect.left = 1515
            textRect.top = 30+300*j
            screen.blit(text, textRect)

            propertyHelper(1755, 60+300*j,i.properties,-1,board,screen, sprites)
            j+=1


def drawDice(dice1, dice2, screen, sprites):
    if dice1 != 0:
        img = sprites['Dice' + str(dice1) + '.png'].copy()
        screen.blit(img, (805, 955))

        img = img = sprites['Dice' + str(dice2) + '.png'].copy()
        screen.blit(img, (1015, 955))

def rollDiceAnimation(screen, sprites):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        img = sprites['Dice' + str(dice1) + '.png'].copy()
        screen.blit(img, (805, 955))

        img = img = sprites['Dice' + str(dice2) + '.png'].copy()
        screen.blit(img, (1015, 955))


def displayProperty(mouseX, mouseY, screen, sprites):
    img = NULL
    #First Row
    if mouseY <= 920 and mouseY >= 800:
        #Medi
        if(mouseX <= 1298 and mouseX >= 1223):
            img = sprites['1Card.png'].copy()
        #Baltic
        if(mouseX <= 1148 and mouseX >= 1073):
            img = sprites['3Card.png'].copy()

    if img != NULL:
        screen.blit(img, (810, 300))  