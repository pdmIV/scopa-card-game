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
        self.colors = ['clubs', 'spades', 'gold coins', 'cups']
        self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.num_cards_in_deck = 40

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

class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards = set()
        self.str_cards = ""
        self.num_cards = 0

    def recieve_card(self, card: Card):
        self.cards.add(card)
        if self.num_cards == 0:
            self.str_cards += card.as_str()
        else:
            addition = ", " + card.as_str()
            self.str_cards += addition
        self.num_cards += 1
    
    
    def reveal(self):
        return self.str_cards


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = list()
        self.pile = set()

    def add_player(self, name: str):
        self.players.append(Player(name))

    def deal(self, amount=1):
        if amount <= self.deck.num_cards_in_deck:
            amt = amount
            while amt > 0:
                for p in self.players:
                    p.recieve_card(self.deck.cards.popleft())
                    self.deck.num_cards_in_deck -= 1
                amt -= 1
        else:
            print("Not enough cards in deck to deal (possibly an error?)")

    def shuffle_deck(self):
        self.deck.shuffle()
    
    def reveal_state(self):
        for player in self.players:
            print(player.name + " posesses " + player.reveal())

# Run Program - example 3 player game with a shuffled deck
game = Game()

game.add_player("Peter")
game.add_player("Sofia")
game.add_player("Francesco")

game.shuffle_deck()

game.deal(3)
game.reveal_state()
            