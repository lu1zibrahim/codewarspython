def descending_order(num):
    s =[int(i) for i in str(num)]
    s.sort(reverse=True)
    numb =[str(x) for x in s]  
    st = "".join(numb)
    return int(st)



# vi essa na net
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))