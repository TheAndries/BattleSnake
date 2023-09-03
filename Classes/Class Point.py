## What is this class defining? 
## Snake length, Snake health, Coordinates per Head, Tail and Body, Coordinates of Food 

class Point:
    def __init__(self, x, y, length, head, tail, health,):
        self.x = x
        self.y = y
        self.length = length
        self.head = head
        self.tail = tail
        self.health = health

## Need to be able to substract, divide, multiply
    def CalcDistance(x, y):
        Distance = (self.x - x) + (self.y - y)

## Coordinates of Head = 0,0 + down, up, left or right
## Coordinates of body = last coordinates of head + 1 if food is eaten
## Coordinates of Tail = last coordinates of body


## Starting length so always 3 + x
length = 3

## Starting coordinates always 0,0 
Head = [0,0]

## starting health always 100 
Health = 100 

## Health per turn = health - 1 
NewHealth = Health - 1 