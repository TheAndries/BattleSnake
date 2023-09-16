## What is this class defining? 
## Only use class for things that we want to multiple times. 
## Snake length, Snake health, Coordinates per Head, Tail and Body, Coordinates of Food 

class Point:
    def __init__(self, x: int, y: int):
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