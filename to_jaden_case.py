def to_jaden_case(string):
    s = string.split()
    k = []
    for word in s:
        letter = word[0].upper() + word[1:]
        k.append(letter)
    st = " ".join(k)
    print(st)



#Vi essa na net


def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())