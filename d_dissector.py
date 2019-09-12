def d_dissector(x):
    dstring = x
    dstring_num = dstring.split('d')[0]
    dstring_dice = dstring.split('d')[1]
    if '+' in dstring_dice:
        dstring_mult = dstring_dice.split('+')[0]
        dstring_bonus = dstring_dice.split('+')[1]
    elif '-' in dstring_dice:
        dstring_mult = dstring_dice.split('-')[0]
        dstring_bonus = dstring_dice.split('-')[1]
    else:
        dstring_mult = dstring_dice
        dstring_bonus = 0
    print(dstring)
    print(dstring_num)
    print(dstring_dice)
    print(dstring_mult)
    print(dstring_bonus)

d_dissector('4d8+2')
