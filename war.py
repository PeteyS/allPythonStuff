values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

import random

class Card(): #card class creates card objects. Creates a card with a suit and rank(string number), and finds the value corrosponding with that rank from the value dictionary

    def __init__ (self,suit,rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank] #self.value attribute gets its value from the values dictionary, which is a global variable, using rank as the key

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck(): #deck class creates 52 card objects, holds all cards as a list, shuffle deck and hand out cards from deck
    
    def __init__ (self):

        self.all_cards = [] #create a list that will be used to append card objects

        for suit in suits: #iterate through every suit, but for every suit
            for rank in ranks: #iterate thorugh every rank for every suit
                #then append that card object so the all cards list so that we get every rank at every suit in the list, creating a 52 card deck
                self.all_cards.append(Card(suit,rank))

    def shuffle(self): #this method will suffle the deck object

        random.shuffle(self.all_cards) #random.shuffle is the same as doing from random import shuffle then doing shuffle(self.all_cards)

    def deal(self): #this deals one card at a time
        return self.all_cards.pop() #this will pop the card, printing its value and remove it from the deck object

class Player(): #class that encompasses all player actions and player environment

    def __init__(self, name): #create a player with a name and give them a list that will hold their cards
        self.name = name
        self.all_cards = []
    
    def remove_one(self): #remove one removes a card from the player deck
        return self.all_cards.pop(0) #pop at index 0 removes card from what would be the top of the deck

    def add_cards(self,new_cards): #add cards adds cards to the player deck (in this case the list)
        
        if type(new_cards) == type([]): #if the players are at war and there are multiple card objects ( if new_cards is a list )
            self.all_cards.extend(new_cards) #use extend to add that list to the all_cards list that holds the players cards. Extend is like zip, lets you add lists without having a nested list in the main list
        else:
            self.all_cards.append(new_cards) #otherwise, if there is just one card, append it to the bottom of deck, in this case the end of the list since it wont add a nested list

    def __str__(self): #defines the string repersentation of the object
        return f'Player {self.name} has {len(self.all_cards)} cards. '

p1 = Player("One") #create player objects
p2 = Player('Two')


new_deck = Deck() #creating deck
new_deck.shuffle()#shuffling the deck

for x in range(26): #splitting the cards between the two players decks
    p1.add_cards(new_deck.deal())
    p2.add_cards(new_deck.deal())

game_on = True #key used for the while loop, while no one has won keep game running

round_number = 0 #round number used to display number of rounds that have been played

while game_on: #while no one has won

    round_number +=1 #add one to round counter, will always start at round 1
    print (f'Round {round_number}')

    if len(p1.all_cards) == 0: #if p1 deck is empty, they lose
        print ('Player 1 out of cards. Player 2 wins')
        game_on = False #turn game on off
        break #and break out of the while loop
    elif len(p2.all_cards) == 0:
        print ('Player 2 is out of cards. Player 1 wins')
        game_on = False
        break

    p1_cards = [] #create list that will be used to compare active cards that are currently in play (this is different than the deck, its the cards that are currently being compared)
    p1_cards.append(p1.remove_one())
    p2_cards = []
    p2_cards.append(p2.remove_one())

    at_war = True

    while at_war:

        if p1_cards[-1].value > p2_cards[-1].value:

            # Player One gets the cards
            p1.add_cards(p1_cards)
            p1.add_cards(p2_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False

        elif p1_cards[-1].value < p2_cards[-1].value:
            p2.add_cards(p1_cards)
            p2.add_cards(p2_cards)
            at_war = False
        else:
            print ('WAR!')

            if len(p1.all_cards) < 5:
                print ('Player 1 unable to declare war')
                print ('Player 2 wins')
                game_on = False
                break
            elif len(p2.all_cards) < 5:
                print ('Player 1 unable to declare war')
                print ('Player 2 wins')
                game_on = False
                break
            else:
                for num in range(5):
                    p1_cards.append(p1.remove_one())
                    p2_cards.append(p2.remove_one())