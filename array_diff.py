 def array_diff(a, b):
    my_list = []
    for item in a:
        if item not in b:
            my_list.append(item)
        else:
            continue
    return my_list


# vi na net
 def array_diff(a, b):
    return [x for x in a if x not in b]
