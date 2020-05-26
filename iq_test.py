def iq_test(numbers):
    my_list = (numbers.split())
    my_even_numbers = []
    my_odd_numbers = []
    for num in my_list:
        if int(num) % 2 == 0:
            my_even_numbers.append(int(num))
        else:
            my_odd_numbers.append(int(num))
    if len(my_even_numbers) > len(my_odd_numbers):
        return my_list.index(str(my_odd_numbers[0]))+1
    else:
        return my_list.index(str(my_even_numbers[0]))+1


# vi na net

def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
