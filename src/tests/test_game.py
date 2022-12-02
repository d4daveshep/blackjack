import pytest

from blackjack.game import Blackjack
from blackjack.player import Player


@pytest.fixture(params=[1, 3, 6])
def game(request):
    min_bet = 5.00
    return Blackjack(number_of_packs=request.param, min_bet=min_bet)


def test_create_blackjack_game(game):
    assert game
    assert game.min_bet == 5.0


def test_game_has_dealer(game):
    assert game
    assert game.dealer


def test_game_dealer_has_correct_number_of_cards(game):
    assert game.dealer.number_of_cards_left() == game.number_of_packs_in_use * 52


def test_add_player_to_game(game):
    assert game
    player = Player("Test", 100.0)
    game.add_player(player)
    assert game.get_player("Test") == player
