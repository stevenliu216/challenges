class Card:
    def __init__(self, suit, rank):
        # This is the initialization object
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        # Return "<rank> of <suit>"
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        # This is the initialization object
        # Initialize the list that will be used to create the deck
        self.cards = []
        self.rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suit = ['hearts', 'clubs', 'diamonds', 'spades']

        self.populate()

    def populate(self):
        # Populate the cards list
        self.cards = [Card(i,j) for i in self.suit for j in self.rank]

    def __repr__(self):
        # Return the whole Deck
        return str(self.cards)
