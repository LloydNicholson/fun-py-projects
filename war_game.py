import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        # self.cards = []
        # for r in RANKS:
        #     for s in SUITE:
        #         self.cards.append(r + s)
        self.cards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def cut(self):
        return self.cards[:26], self.cards[26:]


class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f'Contains {len(self.cards)} cards'

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return 'O', '1'


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def has_cards(self):
        return len(self.hand.cards) != 0

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f'{self.name} has placed: {drawn_card}')
        print('\n')
        return drawn_card


######################
#### GAME PLAY #######
######################

def play_game():
    print("Welcome to War, let's begin...")

    # Use the 3 classes along with some logic to play a game of war!
    deck = Deck()
    deck.shuffle()
    print('SHUFFLING DECK')
    half1, half2 = deck.cut()
    comp = Player('computer', Hand(half1))

    name = input('What is your name?')
    user = Player(name, Hand(half2))

    total_rounds = 0
    war_count = 0

    while user.has_cards() and comp.has_cards():
        total_rounds += 1
        print('Time for a new round')
        print('Here are the current standings')
        print(f'{user.name} has the count: {len(user.hand.cards)}')
        print(f'{comp.name} has the count: {len(comp.hand.cards)}')
        print('Play a card')
        print('\n')

        table_cards = []

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        # Add to table cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # comparing the tuples ranking at index 1
        if c_card[1] == p_card[1]:
            war_count += 1

            print('War')

            # add war cards to the table cards
            table_cards.extend(user.remove_war_cards())
            table_cards.extend(comp.remove_war_cards())

            # Play cards
            c_card = comp.play_card()
            p_card = user.play_card()

            # Add to table cards
            table_cards.append(c_card)
            table_cards.append(p_card)

            if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
                user.hand.add(table_cards)
            else:
                comp.hand.add(table_cards)
        else:
            if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
                user.hand.add(table_cards)
            else:
                comp.hand.add(table_cards)

    print(f'GAME OVER, number of rounds: {total_rounds}')
    print(f'a war happened {war_count} times')
    print('Does the computer still have cards?')
    print(str(comp.has_cards()))
    print('Does the human player still have cards?')
    print(str(user.has_cards()))


play_game()
