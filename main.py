import deck
import player


def check_for_bust(player):
    if player.cards_sum() > 21:
        return True
    else:
        return False


def check_for_eye(player):
    if player.cards_sum() == 21:
        return True
    else:
        return False


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

        print("Computer start sum %d" % computer.cards_sum())
        print("Player start sum %d" % player_one.cards_sum())

        while True:
            bet_choice = float(input("Type your bet: "))
            if type(bet_choice) == float and bet_choice > 0:
                if player_one.make_bet(bet_choice):
                    break
                else:
                    print("Player balance %d" % (player_one.player_pocket.balance))
            else:
                print("Wrong input!\n")

        """
        Player turn
        """
        player_bust = False
        player_eye = False
        player_win = False

        while True:
            player_choice = input("Type Y for next card or N for pass: ")
            if player_choice.capitalize() == "Y":
                player_one.take_card(board_deck.return_one())
                if check_for_bust(player_one):
                    player_bust = True
                    break
                if check_for_eye(player_one):
                    player_eye = True
                    player_win = True
                    break
            elif player_choice.capitalize() == "N":
                break
            else:
                print("Wrong input!\n")

            print("Player [%d]" % player_one.cards_sum())
        
        print("Player [%d]" %player_one.cards_sum())

        """
        Computer turn
        """
        if player_eye == False and player_bust == False:
            while True:
                if player_one.cards_sum() >= computer.cards_sum():
                    computer.take_card(board_deck.return_one())
                else:
                    break
                if check_for_bust(computer):
                    player_win = True
                    break
                if check_for_eye(computer):
                    player_win = False
                    break
                print("Computer [%d]" % computer.cards_sum())
                
            print("Computer [%d]" % computer.cards_sum())

        if player_win:
            player_one.player_pocket.deposit(float(bet_choice))
            print("Player WIN!\n")
        else:
            print("Computer WIN!\n")

        player_one.flush_cards()
        computer.flush_cards()


if __name__ == "__main__":
    game()