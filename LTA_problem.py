"""

4. Given a list of numbers in random order write a linear time algorithm to find the 𝑘th smallest number in the list.
   Explain why your algorithm is linear.
5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?

"""
import random as r


def partition(lst, low, high):
    i = (low - 1)
    card = lst[high]

    for j in range(low, high):

        if lst[j] <= card:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i+1]
    return i + 1


def quick_sort(lst, low, high):
    """
    :param lst: list to be sorted
    :param low: 0
    :param high: (length of list) -1
    :return:
    """
    if len(lst) == 1:
        return lst
    if low < high:
        pari = partition(lst, low, high)
        quick_sort(lst, low, pari - 1)
        quick_sort(lst, pari + 1, high)


def quick_test():
    lst = [4, 8, 6, 34, 67, 86, 33, 10]
    n = len(lst)
    print(f"Unsorted: {lst}")
    quick_sort(lst, 0, n - 1)
    print(f"Sorted: {lst}")


def kth_small(k):
    """
    :param k: an int between 0 and 9
    :return: the kth smallest element of a list with length 10
    """
    lst = []
    for i in range(10):
        lst.append(r.randint(1, 100))
    print(f"random list: {lst}")
    quick_sort(lst, 0, 9)
    print(f"ordered list: {lst}")
    print(f"kth smallest element of list: {lst[k-1]}")


if __name__ == '__main__':
    # quick_test()
    kth_small(1)
    kth_small(5)
    kth_small(3)
    kth_small(10)


