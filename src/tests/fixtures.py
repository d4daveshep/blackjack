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
    return {"10": Card(CardNames.Ten, Suits.Spades), "6": Card(CardNames.Six, Suits.Spades),
            "K": Card(CardNames.King, Suits.Spades), "A": Card(CardNames.Ace, Suits.Spades)}


@pytest.fixture()
def hand_blackjack(cards):
    return Hand([cards["10"], cards["A"]])


@pytest.fixture()
def hand_K_10(cards):
    return Hand([cards["K"], cards["10"]])


@pytest.fixture()
def hand_10_6(cards):
    return Hand([cards["10"], cards["6"]])

