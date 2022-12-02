import enum
from typing import Any

from blackjack.card_dealer import CardDealer
from blackjack.pack import Pack
from blackjack.player import Player


class Blackjack:
    def __init__(self, number_of_packs: int, min_bet: float = 5.00):
        self.__min_bet = min_bet
        self.__number_of_packs = number_of_packs
        self.__dealer = CardDealer(number_of_packs)  # the dealer creates and stores the cards
        self.__players = {}


    @property
    def number_of_packs_in_use(self) -> int:
        return self.__number_of_packs

    @property
    def min_bet(self) -> float:
        return self.__min_bet

    @property
    def dealer(self) -> CardDealer:
        return self.__dealer

    def get_player(self, name: str) -> Player:
        return self.__players.get(name)

    def _use_stacked_deck(self):
        pass

    def add_player(self, player: Player):
        self.__players[player.name] = player

    def start(self):
        pass

    def display_hands(self):
        pass

    def number_of_cards_left(self) -> int:
        return len(self.__cards)



# class Hand:
#     def __init__(self, cards: list):
#         self.__cards = cards
#
#     def __len__(self):
#         return len(self.__cards)
#
#     def add(self, card ) -> None:
#         self.__cards.append(card)
#
#     def aces(self) -> list:
#         return list(filter(lambda card: card.is_ace(), self.__cards))
#
#     def is_soft(self) -> bool:
#         return bool(self.aces())
#
#     def is_hard(self) -> bool:
#         return not bool(self.aces())
#
#     def is_blackjack(self) -> bool:
#         """
#         Blackjack hands contain 2 cards, an Ace and a 10 or picture card
#         """
#         if len(self) == 2 and len(self.aces()) == 1 and self.hard_value() == 21:
#             return True
#         else:
#             return False
#
#     @property
#     def value(self) -> int:
#         total = 0
#         for card in self.__cards:
#             total += card.value
#
#         # if total > 21 and self.aces():
#         #     for i in self.aces():
#         #         total -= 10
#         #         if total <= 21:
#         #             break
#
#         return total
#
#     def hard_value(self) -> int:
#         value = self.value
#         for _ in self.aces():
#             value += 10
#             if value > 11:
#                 break
#         return value
#
#     def soft_value(self) -> int:
#         return self.value
#
#     def max_value(self) -> int:
#         return self.value + len(self.aces()) * 10
#
#
# class Move(enum.Enum):
#     Hit = "Hit"
#     Stand = "Stand"
#     Bust = "Bust"
#
#
# class Strategy:
#     @classmethod
#     def decide_move(cls, hand: Hand) -> Move:
#         if hand.value < 17:
#             return Move.Hit
#         elif hand.value <= 21:
#             return Move.Stand
#         else:
#             return Move.Bust
