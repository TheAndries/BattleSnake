from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    #active function by putting in object(head) and gives us its up, left, down, right points
    def get_neighbours(self) -> List["Point"]:
        NextRight = Point(self.x + 1,self.y)
        NextLeft = Point(self.x - 1, self.y)
        NextUp = Point(self.x, self.y + 1)
        NextDown = Point(self.x, self.y - 1)
        return [NextDown, NextUp, NextLeft, NextRight]
    
    def get_direction(self, otherPoint: "Point") -> str:
        if otherPoint.x < self.x:
            return "left"
        if otherPoint.x > self.x:
            return "right"
        if otherPoint.y < self.y:
            return "down"
        if otherPoint.y > self.y:
            return "up"
        else:
            return "up"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()

#Returns distance, use to calculate in how many turns we can be somewhere
    def CalcDistance(self, x, y):
        coordinates = (self.x - x) + (self.y - y)
        return coordinates