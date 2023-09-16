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
from scipy import spatial

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
    my_head = game_state['you']['body'][0]  # Coordinates of your head. grabs first row of body
    my_body = game_state['you']['body'][1:] # grabs head + all of body
    board_height = game_state['board']['height']
    board_width = game_state['board']['width']
    snakes = game_state['board']['snakes']
    foods = game_state['board']['food']
        
    possible_moves = { 
        "up": {
            "x": my_head["x"],
            "y": my_head["y"] + 1,
        }, 
        "down": { 
            "x": my_head["x"],
            "y": my_head["y"] - 1,
        }, 
        "left": { 
            "x": my_head["x"] - 1,
            "y": my_head["y"]
        }, 
        "right": {
            "x": my_head["x"] + 1,
            "y": my_head["y"]
        }
    }
    possible_moves = avoid_my_body(my_body, possible_moves)
    possible_moves = avoid_walls(board_width, board_height, possible_moves)
    possible_moves = avoid_snake(snakes, possible_moves)
    
    target = get_target_close(foods, my_head)

    if len(possible_moves) > 0:
        if target is not None:
            move = move_target(possible_moves, my_head, target)
        else:
            possible_moves = list(possible_moves.keys())
            move = random.choice(possible_moves)
    else:  
        move = "up"
        print('We are going to lose!!')
    
    print(f"{game_state['game']['id']} MOVE {game_state['turn']}: {move} picked from all valid options in {possible_moves}")
    return {"move": move}

def avoid_snake(snakes, possible_moves):
    remove = []

    for snake in snakes:
        for direction, location in possible_moves.items():
            if location in snake["body"]:
                remove.append(direction)

    remove = set(remove)            #removes duplicates
    for direction in remove:
        del possible_moves[direction]

    return possible_moves

def avoid_my_body(my_body, possible_moves):
    remove = []

    for direction, location in possible_moves.items(): 
        if location in my_body:
            remove.append(direction)

    for direction in remove:
        del possible_moves[direction]

    return possible_moves

def avoid_walls(board_width, board_height, possible_moves):
    remove = []

    for direction, location in possible_moves.items():
        x_out_range = (location["x"] < 0 or location["x"] == board_width)
        y_out_range = (location["y"] < 0 or location["y"] == board_height)

        if x_out_range or y_out_range:
            remove.append(direction)
    
    for direction in remove:
        del possible_moves[direction]

    return possible_moves

def get_target_close(foods, my_head):
    coordinates = []

    if len(foods) == 0:
        return None
    
    for food in foods:
        coordinates.append( (food["x"], food["y"]) )

    tree = spatial.KDTree(coordinates)

    results = tree.query([(my_head["x"], my_head["y"])])[1]

    return foods[results[0]] #gives us closest food 

def move_target(possible_moves, my_head, target):
    distance_x = abs(my_head["x"] - target["x"]) #absolute because we want a positive
    distance_y = abs(my_head["y"] - target["y"])

    for direction, location in possible_moves.items():
        new_distance_x = abs( location["x"] - target["x"])
        new_distance_y = abs( location["y"] - target["y"])

        if new_distance_x < distance_x or new_distance_y < distance_y:
            return direction
        
    return list(possible_moves.keys())[0]

if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})


