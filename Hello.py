import random



class GameState():
    def __init__(self, players):
        self.turn = 0
        self.deck = Deck()
        self.players = players
        self.winner = None

    def divide_deck(self):
        random.shuffle(self.deck.cards)
        half = len(self.deck.cards)//2
        first_half = self.deck.cards[:half]
        second_half = self.deck.cards[half:]
        self.players[0].assignStack(first_half)
        self.players[1].assignStack(second_half)
    

        

    def play_game(self):

        def _play_cards(player1, player2, cards = []):
            if len(player1.stack) < 1 or len(player2.stack) < 1:
                if len(player1.stack) > len(player2.stack):
                    self.winner = player1
                else:
                    self.winner = player2
            print("Player 1: " + str(len(player1.stack)))
            print("Player 2: " + str(len(player2.stack)))
            card1 = player1.stack.pop()
            card2 = player2.stack.pop()
            cards.extend([card1, card2])

            if card1.number > card2.number:
                for i in range(len(cards)):
                    player1.stack.append(cards.pop())
                _play_cards(player1, player2)
            elif card1.number < card2.number:
                for i in range(len(cards)):
                    player2.stack.append(cards.pop())
                _play_cards(player1, player2)
            else:
                for i in range(2):
                    if len(player1.stack) < 1 or len(player2.stack) < 1:
                        if len(player1.stack) > len(player2.stack):
                            self.winner = player1
                        else:
                            self.winner = player2
                    card1 = player1.stack.pop()
                    card2 = player2.stack.pop()
                    cards.extend([card1, card2])
                _play_cards(player1, player2, cards)
        
        winner = _play_cards(self.players[0], self.players[1])
        return winner



class Player():
    def __init__(self, name):
        self.name = name
    
    def assignStack(self, stack):
        self.stack = stack

    def take_turn(self):
        pass


class Deck():
    def __init__(self):
        self.cards = []
        for number in range(1, 14):
            for suit in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
                self.cards.append(Card(number, suit))
        


class Card():
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    




if __name__ == "__main__":
    players = [Player("Hugh"), Player("Adam")]
    game = GameState(players)
    game.divide_deck()
    game.play_game()
