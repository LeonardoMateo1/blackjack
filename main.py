class deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"]
        
        self.deck = [(rank, suit) for suit in suits for rank in ranks]

    def __str__(self):
        return str(self.deck)
    
    def shuffle(self):
        import random
        random.shuffle(self.deck)

    def draw(self, n=1):
        cards = self.deck[:n]
        self.deck = self.deck[n:]
        return cards

class hand:
    def __init__(self, cards):
        self.cards = cards

    def add(self, card):
        self.cards.append(card)
    
    def score(self) -> int:
        sum(self.cards)

    def __str__(self):
        return str(self.cards)
    
class player: 
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return str(self.name)
    
class game:
    def __init__(self, num_players):
        self.num_players = num_players

        d = deck()
        d.shuffle()

        self.players = [player(input(f"Enter player {i+1} name: "), hand(d.draw(2))) for i in range(self.num_players)]

    def display_players(self):
        for player in self.players:
            print(player)
            print(player.hand)

if __name__ == "__main__":
    game = game(num_players = int(input("Enter the number of players: ")))
    
    game.display_players()