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

# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "CAsnake",  # TODO: Your Battlesnake Username
        "color": "#888888",  # TODO: Choose color
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }

def start(game_state: typing.Dict):
    print("GAME START")

def end(game_state: typing.Dict):
    print("GAME OVER\n")

# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_body = game_state["you"]["body"][1, :]
    board_height = game_state["board"]["height"]
    board_width = game_state["board"]["width"]
        
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
    
    print_all(game_state, my_head, my_body)

    possible_moves = list(possible_moves.keys())
    if len(possible_moves) > 0:
        return random.choice(possible_moves)
    else:  
        print("GOINT TO LOSE!!!")
        return "Up"

    
def print_all(game_state, my_head, my_body):
    print(f"~~~ Turn: {game_state['Turn']}) Game Mode: {game_state['game']['ruleset']['name']} ~~~")
    print(f"All board game_state this turn: {game_state}")
    print(f"My battlesnakes head this turn is: {my_head}")
    print(f"My battlesnakes head this turn is: {my_body}")

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

    for direction, location in possible_moves.item():
        x_out_range = (location["x"] < 0 or location["x"] == board_width)
        y_out_range = (location["y"] < 0 or location["y"] == board_height)

        if x_out_range or y_out_range:
            remove.append(direction)
    
    for direction in remove:
        del possible_moves[direction]

    return possible_moves

if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})

    # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
    # my_body = game_state['you']['body']

    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
    # opponents = game_state['board']['snakes']

    # Are there any safe moves left?
    #safe_moves = []
    #for move, isSafe in is_move_safe.items():
     #   if isSafe:
      #      safe_moves.append(move)

    #if len(safe_moves) == 0:
     #   print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
     #   return {"move": "down"}

    # Choose a random move from the safe ones


    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
    # food = game_state['board']['food']

#print(f"MOVE {game_state['turn']}: {next_move}")
 #   return {"move": next_move}


# Start server when `python main.py` is run

