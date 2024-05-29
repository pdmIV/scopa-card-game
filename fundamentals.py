import random
from collections import deque


class Card:
    def __init__(self, color, value):
        self.value = value
        self.color = color

    def as_str(self):
        return self.value + " of " + self.color


class Deck:
    def __init__(self, shuffled=False):
        self.colors = ['Bastoni', 'Spada', 'Denari', 'Coppe']
        self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.num_cards_in_deck = 40
        self.pile_values = set()

        self.cards = deque()

        for color in self.colors:
            for value in self.values:
                self.cards.append(Card(color, value))
        
        if shuffled:
            self.shuffle()
    
    def shuffle(self):
        temp_list = list(self.cards)
        random.shuffle(temp_list)
        self.cards = deque(temp_list)

    def build_pile(self, pile: set):
        starting_pile = 4
        while starting_pile > 0:
            card = self.cards.popleft()
            pile.add(card)
            self.pile_values.add(card.value)
            starting_pile -= 1
            self.num_cards_in_deck -= 1

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = set()
        self.matches = set()
        self.str_cards = ""
        self.num_cards = 0

    def recieve_card(self, card: Card):
        self.hand.add(card)
        if self.num_cards == 0:
            self.str_cards += card.as_str()
        else:
            addition = ", " + card.as_str()
            self.str_cards += addition
        self.num_cards += 1
    
    def reveal(self):
        return self.str_cards