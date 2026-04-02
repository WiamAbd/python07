from typing import List

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters battlefield",
        }

    # Combatable
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.damage, incoming_damage)
        damage_taken = incoming_damage - blocked

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": True,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.damage,
            "type": "melee",
        }

    # Magical
    def cast_spell(self, spell_name: str, targets: List[str]) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost,
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            "channeled": amount,
            "total_mana": self.cost + amount,
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.cost,
            "magic_type": "hybrid",
        }
