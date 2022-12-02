import pytest

from blackjack.card import Name
from blackjack.hand import Hand
from fixtures import hand_K_10, hand_10_6, hand_blackjack, hand_2_2, hand_2_3_4_5_6, hand_A_2, hand_A_A, hand_K_4_A_J, \
    cards, shuffled_pack


def test_should_get_aces_in_hand(hand_K_10, hand_blackjack):
    assert hand_K_10.aces() == []
    assert len(hand_blackjack.aces()) == 1


def test_should_be_blackjack(cards):
    blackjack_hand_1 = Hand([cards[Name.ACE], cards[Name.TEN]])
    blackjack_hand_2 = Hand([cards[Name.TEN], cards[Name.ACE]])

    assert blackjack_hand_1.is_blackjack()
    assert blackjack_hand_2.is_blackjack()


def test_should_add_values_of_cards_in_hand(hand_K_10, hand_blackjack, hand_10_6):
    assert hand_blackjack.hard_value() == 21
    assert hand_K_10.value == 20
    assert hand_10_6.value == 16


def test_should_add_values_of_cards_in_hand_with_ACEs(cards):
    hand = Hand([cards[Name.ACE], cards[Name.ACE]])  # 2 ACEs = 2
    assert hand.value == 2

    hand = Hand([cards[Name.ACE], cards[Name.ACE], cards[Name.ACE]])  # 3 ACEs = 3
    assert hand.value == 3

    hand = Hand([cards[Name.ACE], cards[Name.TEN], cards[Name.KING]])
    assert hand.value == 21

    hand = Hand([cards[Name.ACE], cards[Name.TEN], cards[Name.KING], cards[Name.ACE]])
    assert hand.value == 22


def test_hand_values_in_hard_hands(hand_2_2, hand_10_6, hand_K_10, hand_2_3_4_5_6):
    assert hand_2_2.is_hard()
    assert hand_2_2.hard_value() == 4
    assert hand_2_2.soft_value() == 4

    assert hand_10_6.is_hard()
    assert hand_10_6.hard_value() == 16
    assert hand_10_6.soft_value() == 16

    assert hand_K_10.is_hard()
    assert hand_K_10.hard_value() == 20
    assert hand_K_10.soft_value() == 20

    assert hand_2_3_4_5_6.is_hard()
    assert hand_2_3_4_5_6.hard_value() == (2 + 3 + 4 + 5 + 6)
    assert hand_2_3_4_5_6.soft_value() == (2 + 3 + 4 + 5 + 6)


def test_hand_values_in_soft_hands(hand_A_2, hand_blackjack, hand_A_A, hand_K_4_A_J, cards):
    assert hand_A_2.is_soft()
    assert hand_A_2.hard_value() == 13
    assert hand_A_2.soft_value() == 3
    assert hand_A_2.max_value() == 13

    assert hand_blackjack.is_soft()
    assert hand_blackjack.hard_value() == 21
    assert hand_blackjack.soft_value() == 11
    assert hand_blackjack.max_value() == 21

    assert hand_A_A.is_soft()
    assert hand_A_A.soft_value() == 2
    assert hand_A_A.hard_value() == 12
    assert hand_A_A.max_value() == 22

    assert hand_K_4_A_J.is_soft()
    assert hand_K_4_A_J.soft_value() == 25
    assert hand_K_4_A_J.hard_value() == 35
    assert hand_K_4_A_J.max_value() == 35

    hand_K_4_A_A_J = hand_K_4_A_J
    hand_K_4_A_A_J.add(cards[Name.ACE])
    assert hand_K_4_A_A_J.is_soft()
    assert hand_K_4_A_A_J.soft_value() == 26
    assert hand_K_4_A_A_J.hard_value() == 36
    assert hand_K_4_A_A_J.max_value() == 46


# def test_hand_should_draw_two_cards_and_decide_next_move(shuffled_pack):
#     hand = Hand(shuffled_pack.deal_cards(2))
#
#     assert len(hand) == 2
#     move = Strategy.decide_move(hand)
#     if hand.value < 17:
#         assert move == Move.Hit
#     elif hand.value <= 21:
#         assert move == Move.Stand
#     else:
#         assert move == Move.Bust


def test_should_add_card_to_hand(hand_K_10, cards):
    my_hand = hand_K_10
    my_hand.add(cards[Name.ACE])
    assert len(my_hand) == 3
    assert my_hand.soft_value() == 21

    with pytest.raises(ValueError) as error:
        my_hand.add(12)

    pass
