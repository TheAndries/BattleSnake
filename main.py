# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
import typing
from typing import List
from scipy import spatial 
from Classes.Point import Point
from Classes.Snake import Snake
from Classes.GameState import parse_game_state


def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "CAsnake",  
        "color": "#0000FF",  
        "head": "default",  
        "tail": "default",  
    }

def start(game_state: typing.Dict):
    print("GAME START")

def end(game_state: typing.Dict):
    print("GAME OVER\n")

def move(game_state: typing.Dict) -> typing.Dict:
    my_state = parse_game_state(game_state)
    my_head = my_state.you.head
    board_width = my_state.board.width
    board_height = my_state.board.height
    snakes = my_state.board.snakes
    foods = my_state.board.food
    
    possible_moves = my_head.get_neighbours()
    possible_moves = avoid_walls(board_width, board_height, possible_moves)
    possible_moves = avoid_snake(snakes, possible_moves)
    
    target = get_target_close(foods, my_head)
   
    if len(possible_moves) > 0:
        if target is not None:
            move_point = move_target(possible_moves, my_head, target)
            if(move_point is not None):
                move = my_head.get_direction(move_point)
            else:
                move_point = random.choice(possible_moves)
                move = my_head.get_direction(move_point)

        else:
            move_point = random.choice(possible_moves)
            move = my_head.get_direction(move_point)

    else:  
        move = "up"
        print('We are going to lose!!')
    
    print(f"{my_state.game.id} MOVE {game_state['turn']}: {move} picked from all valid options in {possible_moves}")
    return {"move": move}

def avoid_snake(snakes: List[Snake], possible_moves: List[Point]) -> List[Point]:
    to_remove = []
    
    for snake in snakes:
        for location in possible_moves:
            if location in snake.body:
                to_remove.append(location)

    for location in to_remove:
        possible_moves.remove(location)

    return possible_moves


def avoid_walls(board_width: int, board_height: int, possible_moves: List[Point]) -> List[Point]:
    to_remove = [] 

    for location in possible_moves:
        x_out_range = (location.x < 0 or location.x == board_width)
        y_out_range = (location.y < 0 or location.y == board_height)

        if x_out_range or y_out_range:
            to_remove.append(location)

    for location in to_remove:
        possible_moves.remove(location)

    return possible_moves

def get_target_close(foods: List[Point], my_head: Point) -> Point | None:
    coordinates = []

    if len(foods) == 0:
        return None
    
    for food in foods:
        coordinates.append( (food.x, food.y) )

    tree = spatial.KDTree(coordinates)

    results = tree.query([(my_head.x, my_head.y)])[1]

    return foods[results[0]] #gives us closest food 

def move_target(possible_moves: List[Point], my_head: Point, target: Point) -> Point | None :
    distance_x = abs(my_head.x - target.x) #absolute because we want a positive
    distance_y = abs(my_head.y - target.y)

    for location in possible_moves:
        new_distance_x = abs( location.x - target.x)
        new_distance_y = abs( location.y - target.y)

        if new_distance_x < distance_x or new_distance_y < distance_y:
            return location
        
    return None

if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})


