from data import *
from cardClass import *
import random


class Deck():

    deck = []

    def __init__(self):
        self.deck = [Card(s, r) for r in RANKS for s in SUITES]

    def mixDeck(self):
        random.shuffle(self.deck)

    def isEmpty(self):
        return len(self.deck) == 0

    def takeCard(self):
        return self.deck.pop()

    def giveHand(self):
        ranka = []
        for i in range(6):
            korta = self.deck.pop()
            ranka.append(korta)
        return ranka

    def fillHand(self, hand):
        while len(self.hand) != 6:
            if len(self.deck) > 0:
                hand.append(self.deck.takeCard())
            else:
                break
