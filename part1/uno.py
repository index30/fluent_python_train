import collections
import itertools
import random
import sys

Card = collections.namedtuple('Card', ['rank', 'color'])

class Deck:
    nums = [str(i) for i in range(10)]
    syms = ['D2', 'D4', 'R', 'S']
    wilds = ['W', 'W4']
    ranks = nums + nums[1:] + syms + syms
    colors = ['red', 'blue', 'yellow', 'green']
    wildcolors = ['black', 'black', 'black', 'black']

    def __init__(self, *arg):
        self._cards = [Card(rank, color) for (rank, color) in list(itertools.product(self.ranks, self.colors))] + [Card(rank, color) for (rank, color) in list(itertools.product(self.wilds, self.wildcolors))]
        self._players = ['you'] + ['CPU'+str(i) for i in range(int(arg[0][0]))]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def user_len(self):
        return len(self._players)


if __name__=="__main__":
    args = sys.argv[1:]
    if len(args) == 1 and args[0].isdigit():
        deck = Deck(args)
        random = random.choice(deck)
        print(random)
        print(deck._players)
    else:
        print("Error")
