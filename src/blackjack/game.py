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
        return self.__dealer.number_of_cards_left()



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
