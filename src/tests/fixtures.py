import sys

import pytest

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
    hand = Hand()
    hand.add(cards[Name.TEN])
    hand.add(cards[Name.ACE])
    return hand


@pytest.fixture()
def hand_K_10(cards):
    hand = Hand()
    hand.add(cards[Name.KING])
    hand.add(cards[Name.TEN])
    return hand


@pytest.fixture()
def hand_K_10_A(cards):
    hand = Hand()
    hand.add(cards[Name.KING])
    hand.add(cards[Name.TEN])
    hand.add(cards[Name.ACE])
    return hand


@pytest.fixture()
def hand_K_10_A_A(cards):
    hand = Hand()
    hand.add(cards[Name.KING])
    hand.add(cards[Name.TEN])
    hand.add(cards[Name.ACE])
    hand.add(cards[Name.ACE])
    return hand


@pytest.fixture()
def hand_10_6(cards):
    hand = Hand()
    hand.add(cards[Name.TEN])
    hand.add(cards[Name.SIX])
    return hand


@pytest.fixture()
def hand_2_2(cards):
    hand = Hand()
    hand.add(cards[Name.TWO])
    hand.add(cards[Name.TWO])
    return hand


@pytest.fixture()
def hand_2_3_4_5_6(cards):
    hand = Hand()
    hand.add(cards[Name.TWO])
    hand.add(cards[Name.THREE])
    hand.add(cards[Name.FOUR])
    hand.add(cards[Name.FIVE])
    hand.add(cards[Name.SIX])
    return hand


@pytest.fixture()
def hand_A_2(cards):
    hand = Hand()
    hand.add(cards[Name.ACE])
    hand.add(cards[Name.TWO])
    return hand


@pytest.fixture()
def hand_A_A(cards):
    hand = Hand()
    hand.add(cards[Name.ACE])
    hand.add(cards[Name.ACE])
    return hand


@pytest.fixture()
def hand_A_A_A(cards):
    hand = Hand()
    hand.add(cards[Name.ACE])
    hand.add(cards[Name.ACE])
    hand.add(cards[Name.ACE])
    return hand


@pytest.fixture()
def hand_K_4_A_J(cards):
    hand = Hand()
    hand.add(cards[Name.KING])
    hand.add(cards[Name.FOUR])
    hand.add(cards[Name.ACE])
    hand.add(cards[Name.JACK])
    return hand


@pytest.fixture()
def shuffled_pack() -> Pack:
    pack = Pack()
    pack.shuffle()
    return pack
