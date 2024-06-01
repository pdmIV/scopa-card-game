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
            print(player.name + " possesses " + player.reveal())

    def play_turn(self):
        for player in self.players:
            print(f"{player.name}'s turn")
            self.print_pile()
            print(player.reveal(with_nums=True))
            
            # Player chooses a card to play
            while True:
                try:
                    num_choice = int(input("What card do you want to place down? "))
                    if num_choice in player.hand_num_to_card:
                        choice = player.hand_num_to_card.pop(num_choice)
                        player.play_card(choice)
                        print(f"{player.name} placed down {choice.as_str()}")
                        break
                    else:
                        print("Invalid choice, please select a valid card number.")
                except ValueError:
                    print("Invalid input, please enter a number.")

            # Check if the played card has a value lower than all cards in the pile
            if all(choice.value_as_int() < card.value_as_int() for card in self.pile):
                self.pile.add(choice)
                print(f"The card {choice.as_str()} is added to the pile as it is lower than all cards in the pile.")
                print(f"End of {player.name}'s turn\n")
                continue

            # Logic for picking up cards from the pile
            pile_choices = list(self.pile)
            print("Available cards in the pile:")
            for idx, card in enumerate(pile_choices):
                print(f"{idx + 1}) {card.as_str()}")
            
            while True:
                try:
                    pile_choice = int(input("Which card do you want to pick up from the pile? "))
                    if 1 <= pile_choice <= len(pile_choices):
                        chosen_pile_card = pile_choices[pile_choice - 1]
                        if chosen_pile_card.value == choice.value:
                            player.matches.add(choice)
                            player.matches.add(chosen_pile_card)
                            self.pile.remove(chosen_pile_card)
                            print(f"{player.name} picked up {chosen_pile_card.as_str()} from the pile")
                            break
                        else:
                            print("Selected card from the pile does not match. Try again.")
                    else:
                        print("Invalid choice, please select a valid card number.")
                except ValueError:
                    print("Invalid input, please enter a number.")
    
            print(f"End of {player.name}'s turn\n")
    
class PointCounter:
    def __init__(self, game, players: list):
        self.game = game
        self.player_1 = players.pop()
        self.player_2 = players.pop()

    def gold_seven(self):
        if Card("Denari", "7") in self.player_1.matches:
            self.player_1.points += 1
        elif Card("Denari", "7") in self.player_2.matches:
            self.player_2.points += 1

    def scopa(self, player: Player):
        player.points += 1

    def majority_cards(self):
        if len(self.player_1.matches) == len(self.player_2.matches):
            return
        elif len(self.player_1.matches) > len(self.player_2.matches):
            self.player_1.points += 1
        elif len(self.player_1.matches) < len(self.player_2.matches):
            self.player_2.points += 1

    def find_points(self):
        self.gold_seven()
        self.majority_cards()



# Run Program - example 2 player game with a shuffled deck
game = Game()

game.add_player("Player 1")
game.add_player("Player 2")

#pc = PointCounter(game, game.players)

game.shuffle_deck()
game.build_pile()
game.deal(3)

game.play_turn()
