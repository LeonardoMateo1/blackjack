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
        self.card_list = [cards[0], cards[1]]

    def add(self, card):
        self.cards.extend(card)
    
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
    
class dealer:
    def __init__(self, hand):
        self.hand = hand
    
class game:
    def __init__(self, num_players):
        self.num_players = num_players

        d = deck()
        d.shuffle()

        self.dealer = dealer(hand(d.draw(2)))

        self.players = [player(input(f"Enter player {i+1} name: "), hand(d.draw(2))) for i in range(self.num_players)]

    def display_players(self):
        print("Dealer")
        print(self.dealer.hand.card_list[0][0] + " of " + self.dealer.hand.card_list[0][1])
        print("--" * 5)

        for player in self.players:
            print(player.name.title())
            for card in player.hand.cards:
                print(card[0] + " of " + card[1])
            print(f"Current score: {player.hand.score()}")
            print("--" * 5)

    def play(self):
        d = deck()

        for player in self.players:
            print(player.name.title())
            if player.hand.card_list[0][0] == player.hand.card_list[1][0]:
                print("(Split, Hit, Stand)")
            else:
                print("(Hit, Stand)")
            for card in player.hand.cards:
                print(card[0] + " of " + card[1])
            print(f"Current score: {player.hand.score()}")

            while True:
                if player.hand.score() == 21:
                    print("Blackjack!")
                    break
                elif player.hand.score() > 21:
                    print("Bust!")
                    break
                else:
                    self.play = input("What would you like to do? ")

                    if self.play == "Hit":
                        player.hand.add(d.draw(1))
                        print(player.hand)
                        print(f"New score: {player.hand.score()}")
                    elif self.play == "Stand":
                        break


if __name__ == "__main__":
    print("Welcome to Blackjack!")
    game = game(num_players = int(input("How many people are playing? ")))

    print("--" * 5)

    game.display_players()
    game.play()