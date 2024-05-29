from fundamentals import Player, Deck, Card


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = list()
        self.pile = set()

    def add_player(self, name: str):
        self.players.append(Player(name))

    def build_pile(self):
        self.deck.build_pile(self.pile)

    def print_pile(self):
        print("Pile has: \n")
        for card in self.pile:
            print(card.as_str() + "\n")

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
            

    def play_turn(self):
        place_downs_left = 3
        while place_downs_left > 0:
            for player in self.players:
                self.print_pile()
                player.reveal(with_nums=True)
                num_choice = input("What card do you want to place down? \n")
                choice = player.hand_num_to_card.pop(num_choice)
                player.play_card(choice)
                # TODO: Need to create interaction of choosing card to pick up
            place_downs_left -= 1

# Run Program - example 2 player game with a shuffled deck
game = Game()

game.add_player("Player 1")
game.add_player("Player 2")

game.shuffle_deck()
game.build_pile()
game.deal(3)
game.reveal_state()
game.print_pile()