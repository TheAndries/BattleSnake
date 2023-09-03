## What is this class defining? 
## Matrix of the board 
from  Point import Point

class Board:
    def __init__(self, height, width, food, snakes):
        self.height = height
        self.width = width
        self.food = food
        self.snakes = snakes 

    def __str__(self) -> str:
        return f'{self.height} {self.width} {self.food} {self.snakes}' 
    
    def __repr__(self):
        return self.__str__()



#3 potential food spawn points, they have a 25% chance of spawn on the plane
#Can you have the snake move towards food? If so how? Or are those coordinates given to you? 
#if so, input point(GivenCoordinates1), point(GivenCoordinates2), point(GivenCoordinates3)
FoodPoint = [Point(1,3), Point(2,3), Point(3,3)]

print(FoodPoint)