from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===")
    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"\nCreatureCard Info: {card.get_card_info()}")

    mana: int = 6
    print(f"\nPlaying Fire Dragon with {mana} mana available:")
    print(f"Playable: {card.is_playable(mana)}")
    print(
        f"Play result:"
        f"{card.play({'effect': 'Creature summoned to battlefield'})}"
    )

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {card.attack_target('Goblin Warrior')}")

    mana = 3
    print(f"\nTesting insufficient mana ({mana} available): ")
    print(f"Playable: {card.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")
