def countBits(n):
    return [list(bin(n)[2:]).count('1')][0]


# achei na net

def countBits(n):
    return bin(n).count("1")
