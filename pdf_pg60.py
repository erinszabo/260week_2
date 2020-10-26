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


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


"""

def test_enqueue():
    a_queue = Queue()
    start = time.time()
    for i in range(0, 90000):
        a_queue.enqueue(i)
    time.sleep(0.000001)
    end = time.time()
    print(f"Enqueue {end - start} seconds")

"""


# always timed at 0.0 so don't use
def time_decorator(fn):
    def func(x):
        # a_queue = Queue()
        start = time.time()
        fn(x)
        # for i in range(0, 90000):
        #    a_queue.enqueue(i)
        time.sleep(0.000001)
        end = time.time()
        return f"time estimate: {end - start}"  # x,

    return func


"""
### play with this more later ###
def multi_time_decorator(fn):
    def func(x):
        start = time.time()
        for i in range(10):
            x = fn(x)
            i += 1
        end = time.time()
        return x, end - start

    return func
"""


@time_decorator
def sum_of_n_2(num):
    the_sum = 0

    for i in range(1, num + 1):
        the_sum += i

    return the_sum


@time_decorator
def sum2(n):
    return sum(range(1, n + 1))


@time_decorator
def list_index_test(n):
    """
    create a list,
    index at various locations and use time estimate to verify
    the list size is independent of the time it takes to index at any location, O(1)
    :return: String
    """
    lst = []
    # string = f"list size: {size}"
    for i in range(100):
        lst.append("c")
        lst.append("a")
        lst.append("t")
    return print(f"item at index {n}: {lst[n]}")


@time_decorator
def get_test(x):
    """
    create a dictionary,
    get or set various locations and time the task
    :return: String
    """
    dictionary = {
        "meow": "cat",
        "bark": "dog",
        "oink": "pig"
    }
    # print(dictionary)
    return print(f"{dictionary.get(x)}s {x}")


@time_decorator
def del_list_test(x):
    """
    create a list,
    test del operator and time the task
    :type x: int [0,3]
    :return: String
    """
    lst = ["red", "green", "blue", "yellow"]
    del lst[x]
    return print(f"{lst}, element {x} removed")


@time_decorator
def del_dict_test(x):
    """
    create a dictionary,
    test del operator and time the task
    :type x: String "meow", "bark", or "oink" only
    :return: String
    """
    dictionary = {
        "meow": "cat",
        "bark": "dog",
        "oink": "pig"
    }
    del dictionary[x]
    return print(f"{dictionary}, {x} removed")
