"""


"""


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

"""
if __name__ == '__main__':
    quick_test()
"""
