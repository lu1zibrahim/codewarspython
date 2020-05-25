def valid_parentheses(string):
    my_string = list(string)
    count_1 = my_string.count("(")
    count_2 = my_string.count(")")
    if count_1 == count_2:
        return True
    else:
        return False
