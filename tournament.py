def format_opponents(opponents):
    formatted = []
    for f_name, _, s_name, _ in opponents:
        formatted.append(f"({f_name}+{s_name})")
    return " [ " + ", ".join(formatted) + " ]"


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                _, factory1, _, strategy1 = opponents[i]
                _, factory2, _, strategy2 = opponents[j]

                c1 = factory1.create_base()
                c2 = factory2.create_base()

                print("\n* Battle *")
                print(c1.describe())
                print("vs.")
                print(c2.describe())
                print("now fight!")

                strategy1.act(c1)
                strategy2.act(c2)

    except Exception as e:
        print(
            "Battle error, aborting tournament:",
            e
        )


if __name__ == "__main__":
    from ex0 import FlameFactory, AquaFactory
    from ex1 import (
        HealingCreatureFactory,
        TransformCreatureFactory,
    )
    from ex2 import (
        NormalStrategy,
        AggressiveStrategy,
        DefensiveStrategy,
    )

    print("Tournament 0 (basic)")
    opponents = [
        (
            "Flameling",
            FlameFactory(),
            "Normal",
            NormalStrategy(),
        ),
        (
            "Healing",
            HealingCreatureFactory(),
            "Defensive",
            DefensiveStrategy(),
        ),
    ]
    print(format_opponents(opponents))
    battle(opponents)

    print("\nTournament 1 (error)")
    opponents = [
        (
            "Flameling",
            FlameFactory(),
            "Aggressive",
            AggressiveStrategy(),
        ),
        (
            "Healing",
            HealingCreatureFactory(),
            "Defensive",
            DefensiveStrategy(),
        ),
    ]
    print(format_opponents(opponents))
    battle(opponents)

    print("\nTournament 2 (multiple)")
    opponents = [
        (
            "Aquabub",
            AquaFactory(),
            "Normal",
            NormalStrategy(),
        ),
        (
            "Healing",
            HealingCreatureFactory(),
            "Defensive",
            DefensiveStrategy(),
        ),
        (
            "Transform",
            TransformCreatureFactory(),
            "Aggressive",
            AggressiveStrategy(),
        ),
    ]
    print(format_opponents(opponents))
    battle(opponents)
