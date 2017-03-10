import pygame
import winsound
import random
from player import Player
from box import Box
from gate import Gate
from tree import Tree

class Map:
    def __init__(self,width,height):
        self.player = Player(0,0)
        self.box = Box(1,1)
        self.gate = Gate(9,9)
        self.tree = []
        self.ntree = 15
        for i in range (self.ntree):
            while True:
                x = random.randint(1,width-1)
                y = random.randint(1,width-1)
                if not self.player.match(x,y) and not self.box.match(x,y) and not self.gate.match(x,y):
                    break
            self.tree.append(Tree(x,y))
        self.width = width
        self.height = height

    def find_tree(self,x,y):
        for i in range (self.ntree):
            if self.tree[i].match(x,y):
                return i
        return None

    def in_map(self,x,y):
        return 0 <= x < self.width and 0 <= y < self.height and self.find_tree(x, y) == None

    def move_player(self,dx,dy):
        [next_px,next_py] = self.player.calc_next(dx,dy)
        if self.in_map(next_px,next_py):
            if self.box.match(next_px,next_py):
                [next_bx, next_by] = self.box.calc_next(dx, dy)
                if self.in_map(next_bx, next_by):
                    self.box.move(dx, dy)
                    self.player.move(dx,dy)
                    winsound.Beep(200,100)
            else:
                self.player.move(dx,dy)
                winsound.Beep(200,100)

    def check_win(self):
        return self.gate.match(self.box.x,self.box.y)

    def process_input(self,move):
        dx,dy = 0,0
        if move == pygame.K_UP:
            dy = -1
        if move == pygame.K_DOWN:
            dy = 1
        if move == pygame.K_LEFT:
            dx = -1
        if move == pygame.K_RIGHT:
            dx = 1

        self.move_player(dx,dy)