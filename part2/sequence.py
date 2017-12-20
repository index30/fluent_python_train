import random
import sys
sys.path.append('../part1')
from uno import Deck

def make_yourhands(deck):
    # リスト内包表記が2行以上になる場合はfor文を使いましょう
    # わかりづらい表記はダメ
    hand_dict = {}
    for user in deck._players:
        hand = [random.choice(deck) for d in range(7)]
        hand_dict[user] = hand
    # タプルで処理する場合
    # hand_tuple = [(user, [random.choice(deck) for d in range(7)]) for user in deck._players]
    return hand_dict

args = sys.argv[1:]
if len(args) == 1 and args[0].isdigit():
    deck = Deck(args)
    hands = make_yourhands(deck)
    print(hands)
else:
    print("Error")
