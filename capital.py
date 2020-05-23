def capital(capitals):
    counter = 0
    i = len(capitals)
    my_list = []
    while counter < i:
        my_dict = capitals[counter]
        if 'state' in my_dict.keys():
            st = f"The capital of {my_dict['state']} is {my_dict['capital']}"
            my_list.append(st)
            counter +=1
        elif 'country' in my_dict.keys():
            st = f"The capital of {my_dict['country']} is {my_dict['capital']}"
            my_list.append(st)
            counter +=1
        else:
            counter +=1
    return my_list


# vi na net

def capital(capitals):
    return [f"The capital of {c.get('state') or c['country']} is {c['capital']}" for c in capitals]
