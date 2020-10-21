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
import pdf_pg60 as p


def time_decorator(fn):
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end - start

    return func


@time_decorator
def sum_of_n_2(n):
    the_sum = 0

    for i in range(1, n + 1):
        the_sum += i

    return the_sum


@time_decorator
def sum2(n):
    return sum(range(1, n + 1))


print(sum2(100))
print(sum_of_n_2(100))
print(sum_of_n_2(1000))

print(p.list_index_test(2))


if __name__ == '__main__':
    print("")
    print("1. Devise an experiment to verify that the list index operator is 𝑂(1).")
    # p.list_index_test()
    # t1 = Timer("list_index_test()", "from pdf_pg60 import list_index_test")
    # print("list_index_test() ", p.list_index_test.timeit(number=1000), "milliseconds")

    print("2. Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.")
    #
    print("3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.")
    #
    print("4. Given a list of numbers in random order write a linear time algorithm to find the 𝑘th smallest number "
          "in the list. Explain why your algorithm is linear.")
    #
    print("5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?")
    print("")
