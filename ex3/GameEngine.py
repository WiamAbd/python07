from typing import List

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand: List = []
        self.battlefield: List = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured"}

        self.hand = [
            self.factory.create_creature("Fire Dragon"),
            self.factory.create_creature("Goblin Warrior"),
            self.factory.create_spell("Lightning Bolt"),
        ]

        return self.strategy.execute_turn(self.hand, self.battlefield)

    def get_engine_status(self, turn_result: dict) -> dict:
        return {
            "turns_simulated": 1,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": turn_result.get("damage_dealt", 0),
            "cards_created": len(self.hand),
        }
