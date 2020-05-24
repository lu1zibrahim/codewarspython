import math

def is_square(n):
    return n/math.sqrt(abs(n)) == round(math.sqrt(abs(n))) if n!=0 else True


# vi na net

import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;
