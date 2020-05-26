import itertools

def get_pins(observed):
    neighbors = {'1':['1','2','4'],
                '2':['1','2','3','5'],
                '3':['2','3','6'],
                '4':['1','4','5','7'],
                '5':['2','4','5','6','8'],
                '6':['3','5','6','9'],
                '7':['4','7','8'],
                '8':['5','7','8','9','0'],
                '9':['6','8','9'],
                '0':['0','8']}
    observed_numbers = [neighbors [n] for n in observed]
    possible_comb = list(itertools.product(*observed_numbers))
    all_possible_comb = [''.join(n) for n in possible_comb]
    return all_possible_comb


# This one was really hard, and I had to search a solution online, above is the one I came into. can be found in "https://medium.com/@erikgreenj/the-observed-pin-python-challenge-c6baf98dbb8f"
# all credits to do it creator @erikgreenj
# vi na net

def get_pins(observed):
  map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
         ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
  return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]
