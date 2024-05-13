import art
import functions

print(art.logo)

game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

flag = True

if game == 'y':

    while flag:

        flag = True
        user_cards = []
        computer_cards = []

        for i in range(2):

            user_cards.append(functions.deal_card())
            computer_cards.append(functions.deal_card())

        computer_sum = sum(computer_cards)

        if computer_sum < 16:
            computer_cards.append(functions.deal_card())

        functions.player_cards(user_cards)
        functions.dealer_one_card(computer_cards[0])

        if sum(user_cards) == 21:
            print("BLACKJACK!!! You won")
            break

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        while another_card == 'y':
            user_cards.append(functions.deal_card())

            functions.player_cards(user_cards)
            functions.dealer_one_card(computer_cards[0])

            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        player_sum = sum(user_cards)
        computer_sum = sum(computer_cards)

        functions.who_won(player_sum, computer_sum)

        game = input("Do you want play again. 'y' or 'n': ")

        if game == 'n':
            flag = False
