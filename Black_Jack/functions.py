import random


def deal_card():

    cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

    def_card = random.choice(cards)

    return def_card


def player_cards(def_cards):
    print(f"You have {def_cards} sum of your cards are {sum(def_cards)}")


def dealer_one_card(def_cards):
    print(f"Computer's first card is {def_cards}")


def dealer_cards(def_cards):
    print(f"Computer's have {def_cards}, sum of computer's cards are {sum(def_cards)}")


def who_won(def_sum_player, def_sum_computer):

    if def_sum_player > 21:
        print("Computer won, player have to much points.")
        print(f"Player: {def_sum_player}, computer {def_sum_computer}")

    elif def_sum_computer > def_sum_player and def_sum_player < 21:
        print("Computer won, player have to low points.")
        print(f"Player: {def_sum_player}, computer {def_sum_computer}")

    elif def_sum_player == 21:
        print("BLACKJACK!!!! Player won.")
        print(f"Player: {def_sum_player}, computer {def_sum_computer}")

    elif def_sum_player < 21 and def_sum_computer > 21:
        print("Player won, computer have to low points.")
        print(f"Player: {def_sum_player}, computer {def_sum_computer}")

    else:
        print("Player won")
        print(f"Player: {def_sum_player}, computer {def_sum_computer}")
