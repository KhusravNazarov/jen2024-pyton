from random import shuffle
class Card:
     def __init__(self, suits, values):
         self.suits = suits
         self.values = values
     def present(self):
         return f"{self.value} of {self.suit}"
    

class Desk:
     def __init__(self):
         suits = ['hearts', 'diamonds', 'clubs', 'spades']
         values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
         # self.Cards = [Card(suit, value)for suit in suits for value in values ]
         new = []
         for suit in suits:
             all_cards = [(suit, value)for value in values]
             for a in all_cards:
                 new.append(a)    
         self.Cards = new
         
     def shuffle(self):
         shuffle(self.Cards)
         
     def deal(self):
         if self.Cards: # check if list is not empty
             return self.Cards.pop()
         return None    
    
     def count_remaining(self):
         return len(self.Cards)
    def get_remaining(self):
        """Returns a list of string representations of the remaining cards."""
        return [card.present() for card in self.cards]
      
         
         

sample_desk = Desk()         
sample_desk.shuffle()
sample_desk.deal()
print(sample_desk.deal())
print(sample_desk.count_remaining())
print(sample_desk.get_remaining())
# print(sample_desk.Cards)

suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']