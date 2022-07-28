import sys
import pytest

sys.path.append("../")
from blackjack.card import Card, Suits, CardNames
from blackjack.game import Hand, Strategy, Move
from blackjack.pack import Pack


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


def test_should_count_aces_in_hand(hand_K_10, hand_blackjack):
    assert hand_K_10.count_aces() == 0
    assert hand_blackjack.count_aces() == 1


def test_should_add_values_of_cards_in_hand(hand_K_10, hand_blackjack, hand_10_6):
    assert hand_blackjack.value == 21
    assert hand_K_10.value == 20
    assert hand_10_6.value == 16


def test_should_add_values_of_cards_in_hand_with_aces(cards):
    hand = Hand([cards["A"], cards["A"]])  # 2 Aces = 12
    assert hand.value == 12

    hand = Hand([cards["A"], cards["A"], cards["A"]])  # 3 Aces = 13
    assert hand.value == 13

    hand = Hand([cards["A"], cards["10"], cards["K"]])
    assert hand.value == 21

    hand = Hand([cards["A"], cards["10"], cards["K"], cards["A"]])
    assert hand.value == 22


@pytest.fixture()
def shuffled_pack() -> Pack:
    pack = Pack()
    pack.shuffle()
    return pack


def test_hand_should_draw_two_cards_and_decide_next_move(shuffled_pack):
    hand = Hand(shuffled_pack.deal_cards(2))

    assert len(hand) == 2
    move = Strategy.decide_move(hand)
    if hand.value < 17:
        assert move == Move.Hit
    elif hand.value <= 21:
        assert move == Move.Stand
    else:
        assert move == Move.Bust
