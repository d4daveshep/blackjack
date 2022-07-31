import sys
import pytest

sys.path.append("../")
from blackjack.card import Card, Suits, CardNames
from blackjack.game import Hand, Strategy, Move
from blackjack.pack import Pack
from fixtures import hand_K_10, cards, hand_blackjack, hand_10_6, shuffled_pack, hand_2_2, hand_2_3_4_5_6


def test_should_get_aces_in_hand(hand_K_10, hand_blackjack):
    assert hand_K_10.aces() == []
    assert len(hand_blackjack.aces()) == 1


def test_should_be_blackjack(cards):
    blackjack_hand_1 = Hand([cards["Ace"], cards["Ten"]])
    blackjack_hand_2 = Hand([cards["Ten"], cards["Ace"]])

    assert blackjack_hand_1.is_blackjack()
    assert blackjack_hand_2.is_blackjack()


def test_should_add_values_of_cards_in_hand(hand_K_10, hand_blackjack, hand_10_6):
    assert hand_blackjack.value == 21
    assert hand_K_10.value == 20
    assert hand_10_6.value == 16


def test_should_add_values_of_cards_in_hand_with_aces(cards):
    hand = Hand([cards["Ace"], cards["Ace"]])  # 2 Aces = 2
    assert hand.value == 2

    hand = Hand([cards["Ace"], cards["Ace"], cards["Ace"]])  # 3 Aces = 3
    assert hand.value == 3

    hand = Hand([cards["Ace"], cards["Ten"], cards["King"]])
    assert hand.value == 21

    hand = Hand([cards["Ace"], cards["Ten"], cards["King"], cards["Ace"]])
    assert hand.value == 22


def test_hard_values_in_hard_hands(hand_2_2, hand_10_6, hand_K_10, hand_2_3_4_5_6):
    assert False



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

def test_if_hand_is_soft_or_hard(cards):
    soft_hand = Hand([cards["Ace"], cards["Six"]])
    assert soft_hand.is_soft()
    assert not soft_hand.is_hard()
