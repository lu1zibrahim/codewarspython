import string

lst = list(string.ascii_lowercase)

def printer_error(s):

    my_string = list(s)
    counter = 0
    ln = len(my_string)
    if ln > 0:
        for let in my_string:
            if lst.index(let) >12:
                counter +=1
    total = f'{counter}/{ln}'
    return total



#Vi na net

from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
