class InvalidStrategyError(Exception):
    def __init__(self, creature_name: str, strategy: str) -> None:
        super().__init__(
            f"Invalid Creature '{creature_name}' for this {strategy} strategy"
        )
