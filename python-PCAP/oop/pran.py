import random

# Class to represent a single card
class Card:
    def __init__(self, suit, value):
        self.suit = suit   # Suit of the card (e.g., 'hearts', 'diamonds')
        self.value = value # Value of the card (e.g., 'Ace', '2', 'King')

    def present(self):
        """Returns a string representation of the card."""
        return f"{self.value} of {self.suit}"

# Class to represent a deck of 52 cards
class Deck:
    def __init__(self):
        """Initializes the deck with 52 cards."""
        # Suits and values that make up a standard deck of cards
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        
        # List comprehension to create all possible card combinations (52 cards)
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def shuffle(self):
        """Shuffles the deck randomly."""
        random.shuffle(self.cards)
    
    def deal(self):
        """Deals one card from the deck and removes it."""
        if self.cards:
            return self.cards.pop()  # Removes the last card from the deck and returns it
        return None  # If no cards are left, return None
    
    def count_remaining(self):
        """Returns the number of remaining cards in the deck."""
        return len(self.cards)
    
    def get_remaining(self):
        """Returns a list of string representations of the remaining cards."""
        return [card.present() for card in self.cards]

# Example usage
deck = Deck()  # Creating a deck of cards
deck.shuffle()  # Shuffling the deck
print("Remaining cards count:", deck.count_remaining())  # Prints number of remaining cards
print("Remaining cards:", deck.get_remaining()[:5])  # Shows the first 5 cards
dealt_card = deck.deal()  # Dealing one card
print(f"Dealt card: {dealt_card.present() if dealt_card else 'None'}")  # Prints the dealt card
print("Remaining cards count after deal:", deck.count_remaining())  # Prints the count after dealing
