from typing import Dict

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        card_id: str,
        rating: int,
        record: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.id = card_id
        self.rating = rating
        self.record = record

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "effect": "Tournament card in play",
        }

    # Rankable
    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "id": self.id,
            "rating": self.rating,
            "record": self.record,
        }

    # Combatable
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": 5,
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "damage_taken": incoming_damage,
            "still_alive": True,
        }

    def get_combat_stats(self) -> dict:
        return {
            "type": "tournament",
        }

    # Global
    def get_tournament_stats(self) -> Dict:
        return {
            "id": self.id,
            "rating": self.rating,
            "record": self.record,
        }
