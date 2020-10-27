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
import LTA_problem as l


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
    print(p.del_list_test(0))
    print(p.del_list_test(1))
    print(p.del_list_test(2))
    print(p.del_list_test(3))
    print(p.del_dict_test("oink"))
    print(p.del_dict_test("bark"))
    print(p.del_dict_test("meow"))
    print("")

    print("4. Given a list of numbers in random order write a linear time algorithm to find the 𝑘th smallest number "
          "in the list. Explain why your algorithm is linear.")
    l.kth_small(1)
    l.kth_small(5)
    l.kth_small(3)
    l.kth_small(10)
    print("   This algorithm is linear because the big o is O(n log(n)) "
          "meaning the speed is close to linearly dependent on the size of the list")
    print("")

    print("5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))?")
    print("   Since I used a quick sort technique in problem 4, my average should be O(n log(n)) already")
    print("")
