## What is this class defining? 
## Matrix of the board 
from .Snake import Snake
from .Point import Point
from typing import List


class Board:
    def __init__(self, height: int, width: int, food: List[Point], hazards: List[Point], snakes: List[Snake]):
        self.height = height
        self.width = width
        self.food = food
        self.hazards = hazards
        self.snakes = snakes 

    def __str__(self) -> str:
        return f'{self.height} {self.width} {self.food} {self.snakes}' 
    
    def __repr__(self):
        return self.__str__()


