from typing import Dict
from Point import Point
from Game import Game
from Board import Board
from Snake import Snake
from Settings import Settings
from Ruleset import Ruleset
from Customizations import Customizations

class GameState:
    def __init__(self, game: Game, turn: int, board: Board, you: Snake):
        self.game = game
        self.turn = turn
        self.board = board
        self.you = you


def parse_game_state(json_dict: Dict) -> GameState:
    def parse_point(data: Dict) -> Point:
        return Point(data["x"], data["y"])

    def parse_customizations(data: Dict) -> Customizations:
        return Customizations(data["color"], data["head"], data["tail"])

    def parse_snake(data: Dict) -> Snake:
        body = [parse_point(point) for point in data["body"]]
        head = parse_point(data["head"])
        customizations = parse_customizations(data["customizations"])
        return Snake(data["id"], data["name"], data["health"], body, data["latency"], head, data["length"], data["shout"], data["squad"], customizations)

    def parse_settings(data: Dict) -> Settings:
        return Settings(data["foodSpawnChance"], data["minimumFood"], data["hazardDamagePerTurn"])

    def parse_ruleset(data: Dict) -> Ruleset:
        settings = parse_settings(data["settings"])
        return Ruleset(data["name"], data["version"], settings)

    def parse_game(data: Dict) -> Game:
        ruleset = parse_ruleset(data["ruleset"])
        return Game(data["id"], ruleset, data["map"], data["source"], data["timeout"])

    def parse_board(data: Dict) -> Board:
        food = [parse_point(point) for point in data["food"]]
        hazards = [parse_point(point) for point in data["hazards"]]
        snakes = [parse_snake(snake) for snake in data["snakes"]]
        return Board(data["height"], data["width"], food, hazards, snakes)

    game = parse_game(json_dict["game"])
    board = parse_board(json_dict["board"])
    you = parse_snake(json_dict["you"])
    
    return GameState(game, json_dict["turn"], board, you)