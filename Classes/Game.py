## Give summary after a game 
from Ruleset import Ruleset

class Game:
    def __init__(self, id: str, ruleset: Ruleset, map: str, timeout: int, source: str ):
        self.id = id
        self.ruleset = ruleset
        self.map = map
        self.timeout = timeout 
        self.source = source