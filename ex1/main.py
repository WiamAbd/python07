from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


if __name__ == "__main__":
    manager: Deck = Deck()

    manager.add_card(SpellCard("Lightning Bolt", 3, "Rare", "damage"))
    manager.add_card(
        ArtifactCard("Mana Crystal", 2, "Common", 5, "+1 mana per turn")
    )
    manager.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))

    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")
    print(f"Deck stats: {manager.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    card = manager.draw_card()
    print(f"\nDrew: {card.name} (Spell)")
    print(f"Play result: {card.play({})}")

    card = manager.draw_card()
    print(f"\nDrew: {card.name} (Artifact)")
    print(f"Play result: {card.play({})}")

    card = manager.draw_card()
    print(f"\nDrew: {card.name} (Creature)")
    print(f"Play result: {card.play({})}")

    print(
        "\nPolymorphism in action: Same interface, "
        "different card behaviors!"
    )
