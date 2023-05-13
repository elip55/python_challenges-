
import random


# list size is up to the user
# start/stop is the range in which you want the random number to be generated
def make_a_random_list(list_size, start, stop):
    l1 = []
    # first build the list
    for i in range(list_size):
        num = random.randint(start, stop)
        l1.append(num)
    return l1