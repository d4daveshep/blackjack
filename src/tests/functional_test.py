from blackjack.game import Blackjack
from blackjack.card import Face
from blackjack.player import Player

game = Blackjack(number_of_packs=6, min_bet=5.00)
game._use_stacked_deck()  # use a pre-determined order of cards for testing

player1 = Player(name="David", inital_balance=100.00)
game.add_player(player1)
dealer = game.dealer

# play 5 hands
game.start()  # waits for all players to place a bet

# hand 1
player1.place_inital_bet(5.00)  # check balance deducted
player1.receive_card(dealer.deal_card(), Face.UP)
dealer.receive_card(dealer.deal_card(), Face.DOWN)
player1.receive_card(dealer.deal_card(), Face.UP)
dealer.receive_card(dealer.deal_card(), Face.UP)

assert len(player1.hand) == 2
assert len(dealer.hand) == 2

game.display_hands()
exit(0)  #  # if player1.has_blackjack() and dealer.has_blackjack():
#     # stand-off, tie
#     # player receives bet back
#
# elif player1.has_blackjack():
#     # player receives 1.5 x bet
#
# elif dealer.has_blackjack():
#     # player loses bet
#
# else:
#
