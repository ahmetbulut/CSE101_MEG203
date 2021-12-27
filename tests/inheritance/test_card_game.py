from inheritance.card_game import Deck, Card, Hand
from unittest import TestCase

class CardTest(TestCase):

    def test_card_game_init(self):
        # create a deck of 52 cards
        deck = Deck()
        deck.shuffle()

        # invite 2 players to your table; with their hands initially empty.
        Player1 = Hand()
        Player2 = Hand()

        # first time you create a Hand, its set of cards is empty!
        # you are spot checking whether the init works as expected, as it should!
        self.assertEqual(len(Player1.cards), 0)
        self.assertEqual(len(Player2.cards), 0)

    def test_card_game_dealing(self):
        # create a deck of 52 cards
        deck = Deck()
        deck.shuffle()

        # invite 2 players to your table; with their hands initially empty.
        Player1 = Hand()
        Player2 = Hand()

        # the game is on; you deal cards to your players.
        # the players will have non-empty hands.
        num = 4
        deck.deal_cards(Player1, num)
        deck.deal_cards(Player2, num)

        self.assertEqual(4, len(Player1.cards))


