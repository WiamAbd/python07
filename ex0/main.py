from ex0.CreatureCard import CreatureCard
from ex0.Card import Card

if __name__=="__main__":
    print("\n=== DataDeck Card Foundation ===")
    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"\nCreatureCard Info: {card.get_card_info()}")
    print(f"")
    print("\nPlaying Fire Dragon with 6 mana available:")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {card.attack_target("Fire Dragon")}")

    print("\n")

    print("\nAbstract pattern successfully demonstrated!")
