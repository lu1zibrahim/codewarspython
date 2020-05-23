def find_short(s):
    my_list = s.split()
    counter = 0
    min_len = len(my_list[1])
    for word in my_list:
        if min_len > len(word):
            min_len = len(word)
            counter +=1
        else:
            counter +=1
    return min_len



# achei na net

def find_short(s):
    return min(len(x) for x in s.split())
