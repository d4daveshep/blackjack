import sys

import pytest

sys.path.append("../")

from blackjack.card import Card, CardNames, Suits
from blackjack.game import Hand

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
    return Hand([cards[CardNames.Ten], cards[CardNames.Ace]])


@pytest.fixture()
def hand_K_10(cards):
    return Hand([cards[CardNames.King], cards[CardNames.Ten]])


@pytest.fixture()
def hand_10_6(cards):
    return Hand([cards[CardNames.Ten], cards[CardNames.Six]])


@pytest.fixture()
def hand_2_2(cards):
    return Hand([cards[CardNames.Two], cards[CardNames.Two]])


@pytest.fixture()
def hand_2_3_4_5_6(cards):
    return Hand([cards[CardNames.Two], cards[CardNames.Three], cards[CardNames.Four], cards[CardNames.Five],
                 cards[CardNames.Six]])


@pytest.fixture()
def hand_A_2(cards):
    return Hand([cards[CardNames.Ace], cards[CardNames.Two]])


@pytest.fixture()
def hand_A_A(cards):
    return Hand([cards[CardNames.Ace], cards[CardNames.Ace]])


@pytest.fixture()
def hand_K_4_A_J(cards):
    return Hand([cards[CardNames.King], cards[CardNames.Four], cards[CardNames.Ace], cards[CardNames.Jack]])
    

@pytest.fixture()
def shuffled_pack() -> Pack:
    pack = Pack()
    pack.shuffle()
    return pack
