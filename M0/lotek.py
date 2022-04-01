import random

my_nums = {1,40,7,30,21,19}
cost = 3

def random_generator():
    return set(random.sample(range(1,50),k=6))

def counter(my_nums,win_nums):
    how_many=1
    while my_nums!=win_nums:
        win_nums=random_generator()
        how_many+=1
  
    return how_many

if __name__=="__main__":
    machine_nums = random_generator()
    how_many = counter(my_nums,machine_nums)
    print(f'You won after {how_many} attempts.')
    total_cost=how_many*cost
    print(f'You will pay {total_cost} PLN in total.')