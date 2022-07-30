import sys
import pytest

sys.path.append("../")
from blackjack.card import Card, Suits, CardNames
from blackjack.game import Hand, Strategy, Move
from blackjack.pack import Pack
from fixtures import hand_K_10, cards, hand_blackjack, hand_10_6, shuffled_pack


def test_should_get_aces_in_hand(hand_K_10, hand_blackjack):
    assert hand_K_10.aces() == []
    assert len(hand_blackjack.aces()) == 1


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
