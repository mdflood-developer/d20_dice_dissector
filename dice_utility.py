# String parser for dice values in pen and paper RPGs like Pathfinder and Dungeons & Dragons.
# Takes a value like '4d8+2' (which means, in game terms "Roll four eight-sided dice and add two to the final result")
# and returns the values as individual integers in a dictionary
# Also includes functions to roll the dice returned from diceDissector
import random

def diceDissector(dice_roll_value):
    dstring = dice_roll_value
    dstring_num = int(dstring.split('d')[0])
    dstring_dice = dstring.split('d')[1]
    if '+' in dstring_dice:
        dstring_mult = int(dstring_dice.split('+')[0])
        dstring_bonus = int(dstring_dice.split('+')[1])
    elif '-' in dstring_dice:
        dstring_mult = int(dstring_dice.split('-')[0])
        dstring_bonus = int(dstring_dice.split('-')[1])
        dstring_bonus = -dstring_bonus
    else:
        dstring_mult = int(dstring_dice)
        dstring_bonus = 0

    roll_low = (dstring_num * 1) + dstring_bonus
    roll_high = (dstring_num * dstring_mult) + dstring_bonus

    
    dicevalue = {
        'dice':dstring,
        'num_dice':(dstring_num),
        'num_value':(dstring_mult),
        'num_bonus':(dstring_bonus),
        'high':roll_low,
        'low':roll_high
        }
    return dicevalue

def rollDice(dicedata):
    dice_to_roll = dicedata['num_dice']
    value_of_dice = dicedata['num_value']
    bonus_to_add = dicedata['num_bonus']
    total = 0
    for i in range(0,dice_to_roll):
        diceroll = random.randint(0,value_of_dice)
        total += diceroll
    total += bonus_to_add
    if total < 0:
        total = 0
    return total
