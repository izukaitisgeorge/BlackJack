import random

suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}_of_{self.suit}'


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for card in self.deck:
            s += (card.__str__() + "\n")
        return s

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def h_or_s(deck, hand):
    global playing
    try:
        while True:
            x = input('[H]it or [S]tand:  ')
            if x[0].lower() == 'h':
                hit(deck, hand)
            elif x[0].lower() == 's':
                print("You Stand")
                playing = False
            else:
                print("Please Enter H or S:  ")
                continue
            break
    except IndexError:
        print("Please Enter H or S:  ")



def hide_dealer(player, dealer):
    print('DEALER CARDS:')
    print(dealer.cards[1])
    print('--hidden--')
    print('\n')
    print('YOUR CARDS:')
    for card in player.cards:
        print(card)
    print(f'Your total is {player_hand.value}')


def show(player, dealer):
    print('DEALER CARDS:')
    for card in dealer.cards:
        print(card)
    print(f'Your total is {dealer_hand.value}')
    print('\n')
    print('YOUR CARDS:')
    print(player_hand.value)
    for card in player.cards:
        print(card)
    print(f'Your total is {player_hand.value}')


def player_bust(player, dealer):
    print("YOU BUSTED! Dealer wins...")


def dealer_bust(player, dealer):
    print("The Dealer BUSTED! YOU WON!")


def push(player, dealer):
    print("You TIED!")


def player_win(player, dealer):
    print("YOU WON!")


def dealer_win(player, dealer):
    print("OH NO! The dealer won...")


if __name__ == '__main__':
    while True:
        print('Welcome to Blackjack!')

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        hide_dealer(player_hand, dealer_hand)

        while playing:

            h_or_s(deck, player_hand)

            hide_dealer(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_bust(player_hand, dealer_hand)
                break

        if player_hand.value <= 21:
            while dealer_hand.value <= 17:
                hit(deck, dealer_hand)

            show(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_bust(player_hand, dealer_hand)
            elif dealer_hand.value > player_hand.value:
                dealer_win(player_hand, dealer_hand)
            elif dealer_hand.value < player_hand.value:
                player_win(player_hand, dealer_hand)
            else:
                push(player_hand, dealer_hand)

        new_game = input("Play again? y/n: ")
        try:
            if new_game[0].lower() == 'y':
                playing = True
                continue
            elif new_game[0].lower() == 'n':
                print("Play again soon!")
                break
            else:
                new_game = input("Play again? y/n: ")
        except:
            new_game = input("Play again? y/n: ")