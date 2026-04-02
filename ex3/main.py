from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")

    strategy = AggressiveStrategy()
    factory = FantasyCardFactory()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print("\nConfiguring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {result}")

    print("\nGame Report:")
    print(engine.get_engine_status(result))

    print(
        "\nAbstract Factory + Strategy Pattern:"
        " Maximum flexibility achieved!"
    )
