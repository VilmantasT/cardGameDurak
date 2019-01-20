if __name__ == 'main':


    class Card:

        def __init__(self, suite, rank):
            self.suite = suite
            self.rank = rank

        def __gt__(self, other):
            return self.rank > other.rank

        def __str__(self):
            return str(self.suite) + '-' + str(self.rank)
