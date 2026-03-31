from abc import ABC , abstractmethod
from enum import Enum

class Card (ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name =name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass
    def get_card_info(self) -> dict:
        return {'name': self.name, 'cost': self.cost, 'rarity': 'Legendary','type': 'Creature', 'attack': 7, 'health': 5}

    def is_playable(self, available_mana: int) -> bool:
        pass
