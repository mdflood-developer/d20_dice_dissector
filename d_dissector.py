# String parser for dice values in pen and paper RPGs like Pathfinder and Dungeons & Dragons.
# Takes a value like '4d8+2' (which means, in game terms "Roll four eight-sided dice and add two to the final result")
# and returns the values as individual integers in a dictionary

def d_dissector(x):
    dstring = x
    dstring_num = int(dstring.split('d')[0])
    dstring_dice = dstring.split('d')[1]
    if '+' in dstring_dice:
        dstring_mult = int(dstring_dice.split('+')[0])
        dstring_bonus = int(dstring_dice.split('+')[1])
    elif '-' in dstring_dice:
        dstring_mult = int(dstring_dice.split('-')[0])
        dstring_bonus = -int(dstring_dice.split('-')[1])
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
