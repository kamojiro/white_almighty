from copy import deepcopy

def judge(hands):#14 tiles 
    if judge_seven_pairs(hands):
        return True
    for i in range(1,10):
        if hands[i] >= 2:
            if judge_decomposable([ hands[j] - 2 if i == j else hands[j]  for j in range(10)] ):
                return True
    return False

def judge_seven_pairs(hands):
    for i in range(1,10):
        if not ((hands[i] == 2) or (hands[i] == 0)):
            return False
    return True

def judge_decomposable(hands):
    checking_hands = deepcopy(hands)
    for i in range(1,10):
        if checking_hands[i] >= 3:
            checking_hands[i] -= 3
        if checking_hands[i] > 0:
            if i+2 > 9:
                return False
            if (checking_hands[i+1] == 0) or (checking_hands[i+2] == 0):
                return False
            checking_hands[i+1] -= 1
            checking_hands[i+2] -= 1
    return True
