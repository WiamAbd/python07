from typing import List

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> dict:
        cards_played: List[str] = []
        damage_dealt: int = 0

        for card in hand:
            result = card.play({})
            cards_played.append(card.name)

            if "damage" in result.get("effect", "").lower():
                damage_dealt += 3

        return {
            "cards_played": cards_played,
            "mana_used": len(cards_played),
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        return available_targets
