from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    card = EliteCard("Arcane Warrior", 4, "Rare", 5)

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f"Defense result: {card.defend(2)}")

    print("\nMagic phase:")
    print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {card.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
