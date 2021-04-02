import card
import random


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                self.all_cards.append(card.Card(suit, rank))

    def __str__(self):
        output = ""
        for card in self.all_cards:
            output = output + "\n" + str(card)

        return output

    def shuffle(self):
        random.shuffle(self.all_cards)

    def return_one(self):
        return self.all_cards.pop(0)

    
    
