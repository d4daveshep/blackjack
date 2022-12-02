import sys

import pytest

sys.path.append("../")

from blackjack.card import Name, Suit
from blackjack.hand import Hand

from blackjack.pack import Pack


@pytest.fixture()
def pack():
    return Pack()


@pytest.fixture()
def cards():
    pack = Pack()
    card_dict = {}
    for card in pack.show_cards(13):
        card_dict[card.name] = card
    return card_dict


@pytest.fixture()
def hand_blackjack(cards):
    return Hand([cards[Name.TEN], cards[Name.ACE]])


@pytest.fixture()
def hand_K_10(cards):
    return Hand([cards[Name.KING], cards[Name.TEN]])


@pytest.fixture()
def hand_10_6(cards):
    return Hand([cards[Name.TEN], cards[Name.SIX]])


@pytest.fixture()
def hand_2_2(cards):
    return Hand([cards[Name.TWO], cards[Name.TWO]])


@pytest.fixture()
def hand_2_3_4_5_6(cards):
    return Hand([cards[Name.TWO], cards[Name.THREE], cards[Name.FOUR], cards[Name.FIVE],
                 cards[Name.SIX]])


@pytest.fixture()
def hand_A_2(cards):
    return Hand([cards[Name.ACE], cards[Name.TWO]])


@pytest.fixture()
def hand_A_A(cards):
    return Hand([cards[Name.ACE], cards[Name.ACE]])


@pytest.fixture()
def hand_K_4_A_J(cards):
    return Hand([cards[Name.KING], cards[Name.FOUR], cards[Name.ACE], cards[Name.JACK]])
    

@pytest.fixture()
def shuffled_pack() -> Pack:
    pack = Pack()
    pack.shuffle()
    return pack
