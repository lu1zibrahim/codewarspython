def score(dice):
    my_score = 0
    my_list = []
    for num in dice:
        if dice.count(num) >= 3 and num not in my_list:
            my_list.append(num)
        elif num == 1 and dice.count(1) != 3 and num not in my_list:
            my_list.append(num)
        elif num == 5 and dice.count(5) != 3 and num not in my_list:
            my_list.append(num)
    for value in my_list:
        if value != 1 and value != 5:
            my_score += value*100
        elif value == 1 and dice.count(value) >= 3:
            my_score += 1000 + 100*(dice.count(value)-3)
        elif value == 1 and dice.count(value) < 3:
            my_score += 100*dice.count(value)
        elif value == 5 and dice.count(value) >= 3:
            my_score += 500 + 50*(dice.count(value)-3)
        elif value == 5 and dice.count(value) < 3:
            my_score += 50*dice.count(value)

    return my_score


# vi na net

def score(dice):
    return dice.count(1)//3 * 1000 + dice.count(1)%3 * 100 \
           + dice.count(2)//3 * 200 \
           + dice.count(3)//3 * 300 \
           + dice.count(4)//3 * 400 \
           + dice.count(5)//3 * 500 + dice.count(5)%3 * 50 \
           + dice.count(6)//3 * 600 \
