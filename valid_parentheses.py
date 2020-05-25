def valid_parentheses(string):
    if "(" in string and ")" not in string:
        return False
    elif "(" not in string and ")" in string:
        return False
    elif "(" in string and ")" in string:
        my_list = list(string)
        indices_1 = [i for i, x in enumerate(my_list) if x == "("]
        indices_2 = [i for i, x in enumerate(my_list) if x == ")"]
        counter = 0
        my_boo = []
        if len(indices_1) != len(indices_2):
            return False
        else:
            while counter < len(indices_1):
                if indices_1[counter] < indices_2[counter]:
                    counter += 1
                    my_boo.append(1)
                else:
                    counter += 1
                    my_boo.append(2)
            if 2 in my_boo:
                return False

            else:
                return True
    else:
        return True

# Well guys, this one I am ashamed that the solution was so simple yet I struged a lot, down bellow is a very good solution

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
