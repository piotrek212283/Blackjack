import deck
import player


def check_for_bust(player):
    try:
        if (player.cards_sum > 21):
            return True
        else:
            return False
    except:
        print("Pass player object to function")


def check_for_eye(player):
    try:
        if (player.cards_sum == 21):
            return True
        else:
            return False
    except:
        print("Pass player object to function")


def game():

    board_deck = deck.Deck()
    board_deck.shuffle()

    computer = player.Player("Computer", 500)
    player_one = player.Player("Player", 500)

    while True:
        computer.take_card(board_deck.return_one())
        computer.take_card(board_deck.return_one())

        player_one.take_card(board_deck.return_one())
        player_one.take_card(board_deck.return_one())
        
        player_turn = True

        while player_turn:
            player_choice = input("Type Y for next card or N for pass: ")
            if (player_choice is 'Y'):
                player_one.take_card(board_deck.return_one())
                



if __name__ == "__main__":
    game()