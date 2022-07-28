import enum

from blackjack.card import CardNames


class Hand():
    def __init__(self, cards: list):
        self.__cards = cards

    def __len__(self):
        return len(self.__cards)

    def count_aces(self):
        aces = 0
        for card in self.__cards:
            if card.name == CardNames.Ace:
                aces += 1
        return aces

    @property
    def value(self) -> int:
        total = 0
        for card in self.__cards:
            total += card.value

        if total > 21 and self.count_aces():
            for i in range(self.count_aces()):
                total -= 10
                if total <= 21:
                    break

        return total

class Move(enum.Enum):
    Hit = "Hit"
    Sit = "Sit"
    Bust = "Bust"

class Strategy:
    @classmethod
    def decide_move(cls, hand: Hand) -> Move:
        if hand.value < 17:
            return Move.Hit
        elif hand.value <= 21:
            return Move.Sit
        else:
            return Move.Bust



