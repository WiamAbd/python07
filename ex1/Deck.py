from typing import List, Optional
import random

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        creature_count: int = len(
            [card for card in self.cards if isinstance(card, CreatureCard)]
        )
        spell_count: int = len(
            [card for card in self.cards if isinstance(card, SpellCard)]
        )
        artifact_count: int = len(
            [card for card in self.cards if isinstance(card, ArtifactCard)]
        )

        costs: List[int] = [card.cost for card in self.cards]
        avg_cost: float = float(round((sum(costs) + 1) / len(costs)))

        return {
            "total_cards": len(self.cards),
            "creatures": creature_count,
            "spells": spell_count,
            "artifacts": artifact_count,
            "avg_cost": avg_cost,
        }
