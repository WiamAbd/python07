from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


if __name__ == "__main__":
    platform = TournamentPlatform()

    card1 = TournamentCard(
        "Fire Dragon", 1, "Rare", "dragon_001", 1200, "0-0"
    )
    card2 = TournamentCard(
        "Ice Wizard", 1, "Rare", "wizard_001", 1150, "0-0"
    )

    print("\n=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...")
    print(platform.register_card(card1))
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card1.rating}")
    print(f"- Record: {card1.record}")

    print(platform.register_card(card2))
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card2.rating}")
    print(f"- Record: {card2.record}")

    print("\nCreating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        print(
            f"{i}. {card.name} - Rating: {card.rating} ({card.record})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
