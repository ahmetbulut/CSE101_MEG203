import random

class Card:
    """
    Denotes the Card objects in Card games.
    Each card has a suit and a rank.
    """

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    # self < other ?
    def __lt__(self, other):
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        return self.rank < other.rank

class Deck:
    """
    Represents a card game.
    A deck has a set of cards.
    """

    def __init__(self):
        self.cards = [] # empty list
        for suit in range(4): # outer loop
            for rank in range(1, 14): #inner loop
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        representation = []

        for card in self.cards:
            representation.append(str(card))

        return "\n".join(representation)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def deal_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def shuffle(self):
        random.shuffle(self.cards)

class Hand(Deck):
    """
    Represents a player's hand.
    Each hand has a label (Player's name), and a certain subset of cards.
    """

    def __init__(self, label=''):
        self.cards = []
        self.label = label

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

print("------")
print(Player1)
print("------")
print(Player2)
print("------")
