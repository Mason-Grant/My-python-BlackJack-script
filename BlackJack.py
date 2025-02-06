print ("welcome to BlackJack!")
name = input("What's your name?")
print (f'Hello {name}')
Decision = input("do you want to enter the game? yes or no")

while True:
	if Decision == "yes":
		print ("Lets begin!")
		break
	elif Decision == "no": 
		print ("Thats not cool!")
		NewDecision = input("Try again")
		if NewDecision == "yes":
			print ("lets begin!")
			break
		elif Decision == "no":
			print ("Oh dear")
			quit()

# all this stuff before doesnt really matter Im just messing about having fun

import random

#this is just here to define what we are going to be using for the game
suits = ['hearts','diamonds','spades','clubs']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
values = {str(i): i for i in range(2,11)}
values.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})	

deck = [(suit, rank) for suit in suits for rank in ranks]
random.shuffle(deck)
# this is for calculating the hand value
def calculate_hand(hand):
	value = sum(values[card[1]] for card in hand)
	num_aces = sum(1 for card in hand if card[1] == 'A')

# the adjustment for the aces
	while value > 21 and num_aces:
		value -= 10
		num_aces -= 1

	return value

# now this is for dealing cards
def deal_card():
	global deck
	return deck.pop()

#starting game

player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

print(f"yourhand: {player_hand}, value: {calculate_hand(player_hand)}")
print(f"dealer's first card: {dealer_hand[0]}")

#player's turn

while calculate_hand(player_hand) < 21:
    action = input("Hit or Stand? ").lower()
    if action == 'hit':
        player_hand.append(deal_card())
        print(f"Your hand: {player_hand}, Value: {calculate_hand(player_hand)}")
    else:
        break 

#dealers hand

while calculate_hand(dealer_hand) < 17:
	dealer_hand.append(deal_card())

#whose the winner?

player_value = calculate_hand(player_hand)
dealer_value = calculate_hand(dealer_hand)

print(f"\nDealer's hand: {dealer_hand}, value: {dealer_value}")
if player_value > 21:
	print("you are bust! dealer wins!")
elif dealer_value > 21 or player_value > dealer_value:
	print("you win!")
elif dealer_value == player_value:
	print("It's a tie!")
else:
	print("dealer wins")


