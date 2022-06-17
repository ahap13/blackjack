
"""Blackjack Game"""

import random

# Class for the player (There will be one for user and one automatically created for dealer
class player:
    def __init__(self, name, card_total):
        self.name = name
        self.card_total = card_total

    def get_name(self):
        print(self.name)

    def get_card_total(self):
        print(self.card_total)

    def deal_card(self):
        global cards
        cards = {"1": 1,
                 "2": 2,
                 "3": 3,
                 "4": 4,
                 "5": 5,
                 "6": 6,
                 "7": 7,
                 "8": 8,
                 "9": 9,
                 "10": 10,
                 "Jack": 10,
                 "Queen": 10,
                 "King": 10,
                 "Ace": 11}
        card_delt = random.choice(list(cards.keys()))
        if card_delt == "Ace":
            if self.card_total + cards[card_delt] > 21:
                self.card_total = self.card_total + 1
            else:
                self.card_total = self.card_total + cards[card_delt]
        else:
            self.card_total = self.card_total + cards[card_delt]
        return card_delt, cards[card_delt]

    def hit(self, new_card_str, new_card_int): #Number keys are strings to keep uniformity with face cards and easier str concatenation
        print("You recieved a " + new_card_str + ", bringing your total to " + str(self.card_total) + ".")
        if self.card_total > 21:
            print("Unfortunately, this means you busted and the dealer wins.\nThanks for playing!")
            exit()
        if self.card_total == 21:
            print("Congratulations, you win!\nThanks for playing!")
            exit()


# New object for dealer
dealer = player("Dealer", 0)

# Welcome message, choose to continue or read rules
print("Welcome to the Blackjack table. Press 1 to play or 2 to hear the rules.")
user_in1 = input()

if user_in1 == "2":
    print("In Blackjack, the aim of the game is to get closer to 21 than the dealer, without going over.\n"
          "You will initially receive two cards faced up, while the dealer will receive one faced up and\n"
          "one faced down. You will then add up the total of the two cards to get your current total (all\n"
          "face cards = 10 and aces = 11).\n\n"
          "Now you must decide whether you would like to receive another card. You risk going over 21, called\n"
          "a bust, and losing or you may choose to stay and hope that you are closer than the dealer. You may\n"
          "choose to hit as many times as you would like until you choose to stay or you bust.\n\n"
          "Once you choose to stay, the dealer than reveals their faced down card. If the total of their two\n"
          "cards are less than 16, the dealer must hit. If the total is 16 or greater, the dealer must stay\n"
          "If you are closer to 21 or if the dealer busts, you win. If the dealer is closer to 21, you lose\n")
while user_in1 != "1" and user_in1 != "2":
    user_in1 = input("Please enter a valid choice.\n")

print("Now, let's begin.")

user_in2 = "N"
# Print player details to endure it's correct
while user_in2.upper() == "N":
    print("Please enter your name.")
    user_name = input()
    print("You entered " + user_name + ". Is this correct? Enter Y for yes and N for no.")
    user_in2 = input()

player = player(user_name, 0)

print("First, the dealer will deal two cards to you and themself.")

# Only one card will be dealt to the dealer, and the "reveal" of the faced down card will be another deal.
initial_deal1 = player.deal_card()
initial_deal2 = player.deal_card()
initial_deal3 = dealer.deal_card()

print("You received a " + initial_deal1[0] + " and a " + initial_deal2[0] + ".")
print("Your card total is currently " + str(player.card_total) + ".")
if player.card_total == 21:
    print("Congratulations, you won! Thanks for playing!")
    exit()
print("\nThe dealer recieved a " + initial_deal3[0] + " and a face down card.\n")

hit_stay_choice = 0

while hit_stay_choice != "2":
    print("What would you like to do?\n"
          "1. Hit\n"
          "2. Stay")
    hit_stay_choice = input()
    if hit_stay_choice == "1":
        new_card = player.deal_card()
        player.hit(new_card[0], new_card[1])

print("\nYou chose to stay with a card total of " + str(player.card_total) + ".")
print("Let's see what the dealer has.")

# Get dealer's total by flipping over other card
face_down_card = dealer.deal_card()
print("\nThe dealer currently has a " + initial_deal3[0] + " and a faced down card.\n"
        "The dealer flipped the face down card over to reveal a " + face_down_card[0] + ".\n"
        "This brings the dealer's total to " + str(dealer.card_total) + ".")

# If dealer card total is at least 16
if dealer.card_total >= 16:
    if dealer.card_total > player.card_total:
        print("The dealer has won.\nThanks for playing!")
    if dealer.card_total < player.card_total:
        print("You win!\nThanks for playing!")

# Dealer needs to hit until card total is >= 16
while dealer.card_total < 16:
    final_card = dealer.deal_card()
    print("The dealer drew a card and received a " + final_card[0] + ", bringing their total to " + str(dealer.card_total) + ".")
    if dealer.card_total == 21:
        print("The dealer has reached 21. Unfortunately, this means the dealer has won.\nThanks for playing!")
    if dealer.card_total > 21:
        print("The dealer has busted, you win!\nThanks for playing!")
    if dealer.card_total > 15 and dealer.card_total < 21:
        if dealer.card_total > player.card_total:
            print("The dealer has won.\nThanks for playing!")
        if dealer.card_total < player.card_total:
            print("You win!\nThanks for playing!")
