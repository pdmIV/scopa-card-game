import random
from collections import deque


class Card:
    def __init__(self, color, value):
        self.value = value
        self.color = color

    def as_str(self):
        return self.value + " of " + self.color
    def value_as_int(self):
        return int(self.value)


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
        self.hand_num_to_card = dict()
        self.hand = set()
        self.matches = set()
        self.str_cards = ""
        self.num_cards = 0
        self.points = 0

    def recieve_card(self, card: Card):
        self.num_cards += 1
        self.hand_num_to_card[self.num_cards] = card
        self.hand.add(card)
        self.update_str_cards()

    def play_card(self, card: Card):
        self.hand.remove(card)
        # Find the key corresponding to the card and remove it from the hand_num_to_card dict
        key_to_remove = None
        for key, value in self.hand_num_to_card.items():
            if value == card:
                key_to_remove = key
                break
        if key_to_remove:
            del self.hand_num_to_card[key_to_remove]
        self.num_cards -= 1
        self.update_str_cards()

    def update_str_cards(self):
        self.str_cards = ", ".join([card.as_str() for card in self.hand])

    def reveal(self, with_nums=False):
        if not with_nums:
            return self.str_cards
        else:
            pairs = ""
            for key in self.hand_num_to_card:
                pairs += f"{key}) {self.hand_num_to_card[key].as_str()}\n"
            return pairs
    
