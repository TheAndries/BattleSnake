## What is this class defining? 
## Only use class for things that we want to multiple times. 
## Snake length, Snake health, Coordinates per Head, Tail and Body, Coordinates of Food 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()

#Returns distance, use to calculate in how many turns we can be somewhere
    def CalcDistance(self, x, y):
        coordinates = (self.x - x) + (self.y - y)
        return coordinates
    
    #Define out of bounds
    def OutOfBounds(self, x, y):
        if x < 0:
            print('Dont move here')
        if x > 11:
            print('Dont move here')
        else:
            return print('All good on this side') 
        if y < 0:
            print('Dont move here')
        if y > 11:
            print('Dont move here')
        else:
            return print('All good on this side') 

#OutOfBounds = Point([(-1,0:11), (0:11,-1), (12, 0:11), (0:11, 12)])

SnakePoint = Point(12,4)
Try = Point(0,0)

print(SnakePoint)
print(Try.OutOfBounds(12, 4))


## Need to be able to substract, divide, multiply
## Coordinates of body = last coordinates of head + 1 if food is eaten
## Coordinates of Tail = last coordinates of body
## Left left left = -1,0 - -1, 0, -1, 0
## if we are 4 and make circles we will still survive because every square in a 2x2 will be occupied.

## Starting length so always 3 + x
#length = 3

## Starting coordinates always 0,0 
#Head = [0,0]

## starting health always 100 
#Health = 100 

## Health per turn = health - 1 
#NewHealth = Health - 1 