from random import randint

card_faces = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 
              9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}

def deal():
    return randint(1, 13)

def _get_hand_value(cards):
    val = 0
    for card in cards:
        if 1 < card <= 10:
            val += card 
        elif card > 10:
            val += 10 

    if 1 in cards and val + 11 <= 21:
        return val + 11
    elif 1 in cards:
        return val + 1
    else:
        return val    

def show_hand(name, cards):
    faces = [card_faces[card] for card in cards]
    val = _get_hand_value(cards)

    if val == 21:
        note = "BLACK JACK!"
    else:
        note = ""

    print("%s's hand: %s, %s : %s %s" % (name, faces[0], faces[1], val, note))


for name in ("Dealer", "Player"):
    cards = (deal(), deal())
    show_hand(name, cards)



