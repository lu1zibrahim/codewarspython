def disemvowel(string):
    for i in "aeiouAEIOU":
        string = string.replace(i,"")
    return string


# vi na net

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
