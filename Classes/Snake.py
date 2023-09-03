## What is this class defining? See battlesnake webpage

from  Point import Point

class Snake:
    def __init__(self, id, name, health, body, latency, head, length, shout, squad):
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

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.health} {self.body} {self.latency} {self.head} {self.length} {self.shout} {self.tail}' 
    
    def __repr__(self):
        return self.__str__()

name = 'SnakymcMsnake'
body = [Point(1,3), Point(2,3), Point(3,3)]

TailPoint = Snake(1,name,3,body,5,6,7,8,9)
print(TailPoint)

#So we want to prevent the snake from moving into walls. It is a matrix of 11x11.
#Meaning we should have it determine moves as unsafe if:
#Head coordinates + move = NewCoordinates [(-1,0:11), (0:11,-1), (12, 0:11), (0:11, 12)]














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