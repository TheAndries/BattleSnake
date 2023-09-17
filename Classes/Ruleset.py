from .Settings import Settings

class Ruleset:
    def __init__(self, name: str, version: str, settings: Settings):
        self.name = name
        self.version = version
        self.settings = settings