def maskify(cc):
    my_st = list(cc)
    counter = 0
    for i in my_st[:-4]:
        my_st[counter] = "#"
        counter +=1
    my_str = "".join(my_st)
    return my_str



# vi na net

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
