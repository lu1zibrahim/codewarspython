import string

lst = list(string.ascii_lowercase)
ls = list(string.ascii_uppercase)

print(lst,ls)
def find_missing_letter(chars):
    my_list = []
    counter = 0
    if chars[0] in lst:
        for char in chars:
            my_list.append(lst.index(char))
        for num in my_list:
            if my_list[counter] == my_list[counter+1]-1:
                counter+=1
            else:
                return lst[my_list[counter]+1]
    elif chars[0] in ls:
        for char in chars:
            my_list.append(ls.index(char))
        for num in my_list:
            if my_list[counter] == my_list[counter+1]-1:
                counter+=1
            else:
                return ls[my_list[counter]+1]



# vi na net

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
