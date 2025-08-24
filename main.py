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
        score = 0
        for card in self.cards:
            if card[0] == "Ace":
                score += 11
            elif card[0] in ["Jack", "Queen", "King"]:
                score += 10
            else:
                score += int(card[0])
        return score

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
            print(player.name.title())
            for card in player.hand.cards:
                print(card[0] + " of " + card[1])
            print(f"Current score: {player.hand.score()}")
            print("--" * 5)

if __name__ == "__main__":
    print("Welcome to Blackjack!")
    game = game(num_players = int(input("How many people are playing? ")))

    print("--" * 5)

    game.display_players()