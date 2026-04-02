from typing import List

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: List[TournamentCard] = []
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return f"\n{card.name} (ID: {card.id}):"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.matches_played += 1

        card1 = next(card for card in self.cards if card.id == card1_id)
        card2 = next(card for card in self.cards if card.id == card2_id)

        winner = card1 if card1.rating >= card2.rating else card2
        loser = card2 if winner == card1 else card1

        winner.update_wins(1)
        loser.update_losses(1)

        winner.record = "1-0"
        loser.record = "0-1"

        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> List[TournamentCard]:
        return sorted(self.cards, key=lambda c: c.rating, reverse=True)

    def generate_tournament_report(self) -> dict:
        avg_rating = (
            sum(card.rating for card in self.cards) / len(self.cards)
            if self.cards
            else 0
        )

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": round(avg_rating),
            "platform_status": "active",
        }
