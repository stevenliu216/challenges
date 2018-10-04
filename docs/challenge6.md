# Challenge 6

Create a model of a deck of cards that could form the basis for building a digital card game.
In order the accomplish this, use Object-Oriented Programming (OOP). This will make your code
easier to understand, reuse, and change.

### Function prototype:
    class Card:
        def __init__(self, attribute1, attribute2):
            # This is the initialization object
            # Replace attribute1 and 2 with the attributes you need for your cards
            self.attribute1 = attribute1
            self.attribute2 = attribute2
        
        def __repr__(self):
            # Insert return statement here in the output format
    
    class Desk:
        def __init__(self):
            # This is the initialization object
            # Initialize the list that will be used to create the deck
        
        def populate(self):
            # Use this method to populate your deck with cards
 
 
### Return values
Instance of Card (object): The returned card object with representation "number of suit"
Instance of Deck (object): Printed list of cards in deck
 
### Example
##### Sample Input
    my_card = Card("hearts", "6")
    my_deck = Deck()
 
##### Sample Output
    6 of hearts
    [2 of hearts, 3 of hearts, 4 of hearts, 5 of hearts, 6 of hearts, 7 of hearts,
     8 of hearts, 9 of hearts, 10 of hearts, J of hearts, Q of hearts, K of hearts,
     A of hearts, 2 of clubs, 3 of clubs, 4 of clubs, 5 of clubs, 6 of clubs,
     7 of clubs, 8 of clubs, 9 of clubs, 10 of clubs, J of clubs, Q of clubs,
     K of clubs, A of clubs, 2 of diamonds, 3 of diamonds, 4 of diamonds,
     5 of diamonds, 6 of diamonds, 7 of diamonds, 8 of diamonds, 9 of diamonds,
     10 of diamonds, J of diamonds, Q of diamonds, K of diamonds, A of diamonds,
     2 of spades, 3 of spades, 4 of spades, 5 of spades, 6 of spades, 7 of spades,
     8 of spades, 9 of spades, 10 of spades, J of spades, Q of spades, K of spades,
     A of spades]
 
### Explanation
The first input creates a single card and returns it in the format "number of suit".
The second input creates a deck of cards and returns the list of cards in the deck.
