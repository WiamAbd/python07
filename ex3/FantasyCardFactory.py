from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.Card import Card

class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        return CreatureCard(name_or_power, 5, "Legendary", 7, 5)
    
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return SpellCard(name_or_power, 3, "Rare", "damage")
    
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return ArithmeticError(name_or_power, 2, "Common", 5, "+1 mana per turn")
    
    def create_themed_deck(self, size: int) -> dict:
        pass
    
    def get_supported_types(self) -> dict:
        pass
