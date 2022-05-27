#!/bin/python3

import random
import argparse

# Argparse
parser = argparse.ArgumentParser(description='EON OB dice roller.')
parser.add_argument('--t6', type=int, required=False, default=1)
parser.add_argument('--bonus', type=int, required=False, default=0)
args = parser.parse_args()
dicerolls = args.t6
bonus = args.bonus

# Function for ob dice
def ob_dice(dicerolls, bonus):
    list_of_ob_rolls = []
    list_of_sixes = []
    sum = 0
    sixes = 0
    total = 0

    def roll(nr):
        for i in range(nr):
            die=random.randint(1, 6)
            if die == 6:
                list_of_sixes.extend(str(die))
                roll(2)
            else:
                list_of_ob_rolls.extend(str(die))

    # Roll
    roll(dicerolls)
    # Sum dice rolls
    for i in list_of_ob_rolls:
        sum += int(i)
    # count sixes
    for i in list_of_sixes:
        sixes = sixes + 1
    total = sum + bonus
    return sum, list_of_ob_rolls, sixes, total

# Do a barrel roll
sum_rolls, raw_rolls, sixes, total = ob_dice(dicerolls, bonus)
print("Sum   : "+str(sum_rolls))
print("Rolls : "+str(raw_rolls))
print("Sixes : "+str(sixes))
print("Bonus : "+str(bonus))
print("Total : "+str(total))