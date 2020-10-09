"""

1. Devise an experiment to verify that the list index operator is 𝑂(1).
2. Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.
3. Devise an experiment that compares the performance of the del operator on lists and
dictionaries.
4. Given a list of numbers in random order write a linear time algorithm to find the 𝑘th
smallest number in the list. Explain why your algorithm is linear.
5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?

"""

def list_index_test():
    """
    create a list, 
    index at various locations and use timeit to verify that 
    the list size is independent of the time it takes to index at any location, O(1) 
    :return: String
    """
    lst = []
