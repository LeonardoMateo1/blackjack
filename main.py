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

d = deck()
print(d)

d.shuffle()
print(d)

hand = d.draw(2)
print(hand)

class hand:
    def __init__(self, cards):
        self.cards = cards

    def add(self, card):
        self.cards.append(card)
    
    def score(self) -> int:
        sum(self.cards)

    def __str__(self):
        return str(self.cards)
    
