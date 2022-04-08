"""Lotto game

Returns:
    int: cost and number of repetitions in the game
"""

from random import sample

MY_NUMS = {1,40,7,30,21,19}
COST = 3

def random_generator():
    """Generates 6 random numbers to set

    Returns:
        set: six random numbers in range(1,50)
    """
    return set(sample(range(1,50),k=6))

def counter(my_nums,rand_nums):
    """Countes the number of repetitions

    Args:
        my_nums (set): my defined numbers
        random_nums (function): does random_generator() function

    Returns:
        int: numbers of repetitions
    """
    win_nums = rand_nums()
    how_many=1
    while my_nums!=win_nums:
        win_nums=rand_nums()
        how_many+=1

    return how_many

if __name__=="__main__":
    HOW_MANY = counter(MY_NUMS,random_generator)
    print(f'You won after {HOW_MANY} attempts.')
    TOTAL_COST=HOW_MANY*COST
    print(f'You will pay {TOTAL_COST} PLN in total.')
