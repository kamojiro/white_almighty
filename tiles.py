from random import shuffle
from collections import Counter
from itertools import product
from copy import deepcopy
from time import sleep

from judgement import judge

class tiles:
    def __init__(self):
        self.all_tiles = [ i//4 for i in range(40)]
        self.hands = [0]*10 #13 tiles
        self.answer = [False]*10
        self.corresponding_tile = {0:"白 "}
        for i in range(1,10):
            self.corresponding_tile[i] = "" + chr( ord("０")+i) + " "

    def shuffling(self):
        shuffle(self.all_tiles)
        # print(self.all_tiles)
        shuffled_tiles = Counter(self.all_tiles[:13])
        self.hands = [ shuffled_tiles[i] for i in range(10)]
        self.answer = [False]*10
        self.judge_with_white()

    def display_hands(self):
        self.shuffling()
        print("".join( [ self.corresponding_tile[i]*self.hands[i] for i in range(10)]))

    def judge_with_white(self):
        for i in range(1, 10):
            if self.hands[i] == 4 and self.hands[0] == 4:
                continue
            hands_root = deepcopy(self.hands)
            hands_root[i] += 1
            if self.hands[0] == 0:
                if judge( hands_root):
                    self.answer[i] = True
                    continue
            for p in product(range(1,10), repeat=self.hands[0]):
                hands_branch = deepcopy(hands_root)
                for t in p:
                    hands_branch[t] += 1
                if judge( hands_branch):
                    self.answer[i] = True
                    break
        for i in range(1,10):
            if self.answer[i]:
                self.answer[0] = True
                break

    def display_answer(self):
        print("Answer: " + "".join( [ self.corresponding_tile[i] for i in range(10) if self.answer[i]]))
