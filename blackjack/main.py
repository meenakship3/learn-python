############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art

game_start = True # has to be outside because otheriwse the game will run forever


def blackjack_game():
    if (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")) == "y":
        game_start = True
    else:
        print("We're sorry to see you go!")
        game_start = False
    while game_start:
        print(art.logo)
        user_hand = []
        computer_hand = []
        computer_score = 0
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        computer_first_card = random.choice(cards)
        computer_hand.append(computer_first_card)
        computer_score += computer_hand[0]
        while computer_score < 21:
            computer_hand.append(random.choice(cards))
            computer_score = 0
            for i in computer_hand:
                computer_score += i

        for i in range(1, 3):  
            user_card = random.choice(cards)
            user_hand.append(user_card)

        def win_conditions(u_hand, c_hand, u_score, c_score, g_start):
            print(f"Your final hand: {u_hand}, final score: {u_score}")
            print(f"Computer's final hand: {c_hand}, final score: {c_score}")

            if u_score < 21 and c_score < 21:
                if u_score > c_score:
                    print("You win! 😃")
                elif u_score < c_score:
                    print("You lose. 😤")

            elif u_score == c_score:
                print("It's a tie!")

            elif u_score > 21 and c_score < 21:
                print("You went over. You lose. 😭")
            elif c_score > 21 and u_score < 21:
                print("Computer went over. You win! 😃")

            elif u_score > 21 and c_score > 21: 
                print("You both went over. No one wins.")

            elif u_score == 21:
                print("You have a Blackjack! You win! 😃")
            elif c_score == 21:
                print("Computer has a Blackjack! You lose. 😭")

            game_start = False
            blackjack_game()

        def user_moves():
            user_score = 0
            for i in (user_hand):
                user_score += i
            print(f"Your cards: {user_hand}, current score: {user_score}")
            print(f"Computer's first card: {computer_first_card}")
            if user_score < 21:
                another_card = input(
                    "Type 'y' to get another card, type 'n' to pass: ")
                if another_card == "y":
                    user_card = random.choice(cards)
                    user_hand.append(user_card)
                    user_moves()
                elif another_card == "n":
                    win_conditions(user_hand, computer_hand, user_score,
                                   computer_score, game_start)
            elif user_score >= 21:
                win_conditions(user_hand, computer_hand, user_score,
                               computer_score, game_start)
            
        user_moves() 


blackjack_game()

