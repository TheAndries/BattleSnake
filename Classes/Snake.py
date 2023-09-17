## What is this class defining? See battlesnake webpage
from typing import List
from .Point import Point
from .Customizations import Customizations

class Snake:
    def __init__(self, id: str, name: str, health: int, body: List[Point], latency: str, head: Point, length: int, shout: str, squad: str, customizations: Customizations):
        self.id = id 
        self.name = name
        self.health = health
        self.body = body
        self.latency = latency
        self.head = head
        self.length = length
        self.shout = shout 
        self.squad = squad
        self.tail =  body[-1]
        self.customizations = customizations

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.health} {self.body} {self.latency} {self.head} {self.length} {self.shout} {self.tail}' 
    
    def __repr__(self):
        return self.__str__()














## Shout a new message each turn, code either way that is viable 
## So turn = move + shout 
## Or move = move + shout 
Shout = 'Upward and onwards' 


##Coordinates of Head = 0,0 + down, up, left or right
##   def pos_head_after_turn(self, head,):
#       NewPosUp = head + [0,1]
#        NewPosR = head + [1,0]
#        NewPosL = head + [-1,0]
#        NewPosD = head + [0,-1]
        
#        return NewPosD, NewPosUp, NewPosR, NewPosL
    
    ## Coordinates of Tail = last coordinates of body
 #   def pos_head_after_turn(self, tail,):
 #       NewPosUp = tail + [0,1]
  #      NewPosR = tail + [1,0]
   #     NewPosL = tail + [-1,0]
    #    NewPosD = tail + [0,-1]
        
     #   return NewPosD, NewPosUp, NewPosR, NewPosL