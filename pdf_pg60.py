"""

1. Devise an experiment to verify that the list index operator is 𝑂(1).
2. Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.
3. Devise an experiment that compares the performance of the del operator on lists and
dictionaries.
4. Given a list of numbers in random order write a linear time algorithm to find the 𝑘th
smallest number in the list. Explain why your algorithm is linear.
5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?

"""
import time


def time_decorator(fn):
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end - start

    return func


# def time():
#    setup = ""

@time_decorator
def list_index_test(size):
    """
    create a list, 
    index at various locations and use timeit to verify that 
    the list size is independent of the time it takes to index at any location, O(1) 
    :return: String
    """
    lst = []
    # string = f"list size: {size}"
    for i in range(size):
        lst.append("x")
    return lst


print(list_index_test(2))
print(list_index_test(4))
print(list_index_test(6))

""" 
t1 = timeit.Timer(lst[4])
t11 = timeit.Timer("test: ", "from __main__ import test1")
    # print("index 4 took ", t1.timeit(number=1000), "milliseconds")
print("")
print(t1)
print(lst[4])
print(lst)
print(lst.__len__())
list_index_test()
"""