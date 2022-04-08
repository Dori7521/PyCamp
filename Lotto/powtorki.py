"""pylint - sprawdza kod; docstring - pomaga w opisie kodu"""


def my_sum(variable_a,variable_b):
    """adds numbers
    Args:
        variable_a (int): added number
        variable_b (int): added number
    Returns:
        int: sum of the numbers
    """
    return variable_a+variable_b


SCORE = my_sum(2,3)
print(f'Wynik to: {SCORE}')

# Zasada działania if name =="main":
# np funkcje wywołane w tym ifie wywołają się jedynie w tym pliku,
# a nie w tym, gdzie ten plik jest importowany

# Testy jednostkowe
def my_sum(a,b):
    return a+b

# przekazanie funkcji jako argumentu

def to_negative(number):
    return number * -1

def change_to_negative(numbers):
    # new_list = [number*(-1) for number in numbers]
    # return new_list
    return list(map(to_negative,numbers))


def do_something(numbers,function):
    return function(numbers)

print(do_something([1,2,3,4,5,6],sum))
print(do_something([1,2,3,4,5,6],max))
print(do_something([1,2,3,4,5,6],change_to_negative))
