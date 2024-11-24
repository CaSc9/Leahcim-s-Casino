def parse_letters(hand):
    parsing_m = {"J": 11, "Q": 12, "K": 13, "A": 14}
    value = ''  # add logic later
    print(value)
    if value is str:
        return parsing_m[value]
    else:
        return value


# card = [value(2-10 + J=11 Q=12 K=13 A=14   ), suit(s,c,h,d)]
def evaluation(personal_c, community_c):

    hand = personal_c + community_c
    # parse to int

    hand_sorted_value = sorted(hand, key=lambda card: card[0])
    print(hand, hand_sorted_value)


evaluation([[2, "s"], ["Q", "s"]], [[5, "c"]])
