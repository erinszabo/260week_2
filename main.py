"""

1. Devise an experiment to verify that the list index operator is 𝑂(1).
2. Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.
3. Devise an experiment that compares the performance of the del operator on lists and
dictionaries.
4. Given a list of numbers in random order write a linear time algorithm to find the 𝑘th
smallest number in the list. Explain why your algorithm is linear.
5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?

"""
import pdf_pg60 as p


if __name__ == '__main__':
    print("")
    print("1. Devise an experiment to verify that the list index operator is 𝑂(1).")
    print(p.list_index_test(1))
    print(p.list_index_test(10))
    print(p.list_index_test(50))
    print(p.list_index_test(80))
    print(p.list_index_test(99))
    print("")

    print("2. Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.")
    print("get tests:")
    print(p.get_test("meow"))
    print(p.get_test("oink"))
    print(p.get_test("bark"))
    print("")

    print("3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.")
    #
    print("")

    print("4. Given a list of numbers in random order write a linear time algorithm to find the 𝑘th smallest number "
          "in the list. Explain why your algorithm is linear.")
    #
    print("")

    print("5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?")
    #
    print("")
