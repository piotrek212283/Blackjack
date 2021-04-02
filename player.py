import pocket
import card


class Player:
    def __init__(self, name, balance):
        self.name = name
        self.player_pocket = pocket.Pocket(balance)
        self.player_cards = []

    def __str__(self):
        return "Player %s have %d coins with total card sum of %d" % (
            self.name,
            self.player_pocket.balance,
            self.cards_sum,
        )

    def take_card(self, cards):
        if type(cards) == list:
            self.player_cards.extend(cards)
        else:
            self.player_cards.append(cards)

    def cards_sum(self):
        sum = 0
        for i in range(self.player_cards):
            sum += self.player_cards[i].value
