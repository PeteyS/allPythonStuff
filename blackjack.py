import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__ (self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    def __init__(self):
        self.created_deck = []
        for suit in suits:
            for rank in ranks:
                self.created_deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.created_deck)

    def deal(self):
        return self.created_deck.pop(0)

class Player():
    def __init__(self,name):
        self.name = name
        self.player_hand = []
        self.account = 0
        self.number_value = 0
        self.ace_count = 0

    def hit_me(self,new_card):
        self.player_hand.append(new_card)

    def clear_hand(self):
        self.player_hand.clear()
        self.number_value = 0

    def add_money(self,money):
        self.account = self.account + money

    def bet_money (self,money):
        self.account = self.account - money

    def hand_value(self):
        self.number_value = 0
        for obj in self.player_hand:
            self.number_value = self.number_value + obj.value

    def check_ace(self):
        self.ace_count = 0
        for aces in self.player_hand:
            if aces.rank == 'Ace' and self.number_value > 11:
                self.ace_count +=1
        for nums in range(self.ace_count):
            if self.number_value > 10:
                self.number_value - 10
                self.ace_count -=1

def stay_please (player,dealer,bet):
        dealer.hand_value()
        player.hand_value()
        print (f'Dealer hand value is {dealer.number_value}')
        if dealer.number_value > player.number_value and dealer.number_value <21:
            print (f'Dealer wins with a hand value of {dealer.number_value} compared to players hand value of {player.number_value}')
            player.clear_hand()
            dealer.clear_hand()
            return
        elif dealer.number_value == 21:
            print ('Dealer hit 21. Unlucky')
            player.clear_hand()
            dealer.clear_hand()
            return
        while dealer.number_value < player.number_value and dealer.number_value < 17:
            dealer.hit_me(game_deck.deal())
            print (f'Dealer drew a {dealer.player_hand[-1]}')
            dealer.check_ace()
            dealer.hand_value()
            print (f'Dealer hand value is {dealer.number_value}')
            if dealer.number_value == 21:
                print ('Dealer hit 21. Unlucky')
                player.clear_hand()
                dealer.clear_hand()
                return
            elif dealer.number_value > 21:
                print(f'Dealer has gone bust. Player wins {bet * 1.5}')
                player.add_money(bet*1.5)
                player.clear_hand()
                dealer.clear_hand()
                return
            elif dealer.number_value > player.number_value and dealer.number_value < 21:
                print(f"Dealer won with a total hand value of {dealer.number_value} compared to players hand value at {player.number_value}")
                player.clear_hand()
                dealer.clear_hand()
                return
            elif dealer.number_value == player.number_value and dealer.number_value == 21:
                print ('BLACKJACK TIE')
                player.add_money(bet)
        if dealer.number_value == 17 and dealer.number_value < player.number_value:
            print (f'Player wins {bet*1.5}')
            return


def lazy_blackjack_check(player,dealer,bet):
        dealer.hand_value()
        player.hand_value()
        print (f'Dealer hand value is {dealer.number_value}')
        while dealer.number_value < 21:
            dealer.hit_me(game_deck.deal())
            print (f'Dealer drew a {dealer.player_hand[-1]}')
            dealer.check_ace()
            dealer.hand_value()
            print (f'Dealer hand value is {dealer.number_value}')

brand_new_game = True

while brand_new_game:
    player = Player("Player")
    dealer = Player("Dealer")
    game_deck = Deck()
    while True:
        investment= input('How much money would the player like to deposit to start the game. Player account has to have more than zero dollars to play: ')
        try:
            investment = float(investment)
            if investment > 0:
                break
            else:
                print ("Please enter a number greater than zero")
        except :
            print ("Please enter a number")

    
    player.add_money(investment)
    games_begin = True
    i_couldnt_figure_out_how_to_exit_otherwise = True
    while i_couldnt_figure_out_how_to_exit_otherwise:

        while games_begin:

            print (f'Player has ${player.account} in account')
            if player.account == 0:
                print('Player is out of money. Better luck next time')
                i_couldnt_figure_out_how_to_exit_otherwise = False
                games_begin = False
                brand_new_game = False
                break

            while True:
                begin = input("Would you like the hand to begin or would you like to exit? Enter Y to begin or N to exit: ")
                try:
                    if begin.upper() == 'Y':
                        break
                    elif begin.upper() == 'N':
                        break
                except:
                    print ("Please enter Y for yes or N for no")

            if begin.upper() == 'Y':
                games_begin = True
                print ('\n' * 5)
            elif begin.upper() == 'N':
                games_begin = False
                brand_new_game = False
                i_couldnt_figure_out_how_to_exit_otherwise = False
                break

            game_deck.shuffle()
            print ('Deck has been shuffled')

            while True:
                bet = input(f"How much would player like to bet on this hand. Account balance is ${player.account}: ")
                try:
                    bet = float(bet)
                    if bet >0 and bet <= player.account:
                        break
                    else:
                        print ("Please enter a number greater than zero and within your account balance")
                except:
                    print ("Please enter a number greater than zero and within your account balance")

            player.bet_money(bet)
            print (f'Player has bet ${bet}. Account has balance of ${player.account} ')


            player.hit_me(game_deck.deal())
            player.hit_me(game_deck.deal())

            print (player.player_hand[0])
            print (player.player_hand[1])

            (player.hand_value())

            print (f'Current Player hand value is: {player.number_value}')

            dealer.hit_me(game_deck.deal())
            dealer.hit_me(game_deck.deal())


            if player.number_value == 21:
                lazy_blackjack_check(player,dealer,bet)
                if dealer.number_value != 21:
                    print (f'BLACKJACK!')
                    print (f'Player wins ${bet * 2}')
                    player.add_money(bet * 2)
                    player.clear_hand()
                    dealer.clear_hand()
                    break
                elif dealer.number_value == 21:
                    print ('Unlucky. Dealer got Blackjack too')
                    player.clear_hand()
                    dealer.clear_hand()
                    break

            print (f'Dealer is showing {dealer.player_hand[1]}')


            while True:
                hit_me_one_more_time = input (f'Would you like to [h]it or [s]tay. Enter h to hit or s to stay: ')
                try:
                    if hit_me_one_more_time.upper() == "H":
                        break
                    elif hit_me_one_more_time.upper() == 'S':
                        break
                except:
                    print ('Please enter either h to hit or s to stay')


            while hit_me_one_more_time.upper() == 'H':
                print ('Dealer hand is:')
                print (dealer.player_hand[0])
                print (dealer.player_hand[1])
                player.hit_me(game_deck.deal())
                print (f'Player drew a {player.player_hand[-1]}')
                player.hand_value()
                player.check_ace()
                print (f'Player hand value is {player.number_value}')
                if player.number_value > 21:
                    print('Player has gone bust')
                    player.clear_hand()
                    dealer.clear_hand()
                    break
                else:
                    hit_me_one_more_time = input (f'Would you like to [h]it or [s]tay. Enter h to hit or s to stay: ')
                    try:
                        if hit_me_one_more_time.upper() == "H":
                            continue
                        elif hit_me_one_more_time.upper() == 'S':
                            break
                    except:
                        print ('Please enter either h to hit or s to stay')
            if hit_me_one_more_time.upper() == 'S':
                stay_please(player,dealer,bet)
        

