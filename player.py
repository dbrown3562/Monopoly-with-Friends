import pygame

#A player only has an identifier token, money, and a list of properties. And status (jail/no jail).
class Player:
    def __init__(self, id, alias, money, position, properties, color):
        self.id = id
        self.alias = alias
        self.money = money
        self.properties = properties
        self.position = position
        self.jail = False
        self.jailCount = 0
        self.color = color
        self.monopolies = set() #Set of monopolies