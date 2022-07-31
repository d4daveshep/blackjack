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
        card_dict[card.name.name] = card
    return card_dict


@pytest.fixture()
def hand_blackjack(cards):
    return Hand([cards["Ten"], cards["Ace"]])


@pytest.fixture()
def hand_K_10(cards):
    return Hand([cards["King"], cards["Ten"]])


@pytest.fixture()
def hand_10_6(cards):
    return Hand([cards["Ten"], cards["Six"]])


@pytest.fixture()
def hand_2_2(cards):
    return Hand([cards["Two"], cards["Two"]])


@pytest.fixture()
def hand_2_3_4_5_6(cards):
    return Hand([cards["Two"], cards["Three"], cards["Four"], cards["Five"], cards["Six"]])


@pytest.fixture()
def shuffled_pack() -> Pack:
    pack = Pack()
    pack.shuffle()
    return pack
