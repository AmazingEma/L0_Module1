"""
Introduction to lists
"""
import unittest


# TODO Complete the function so it returns a list of any 5 items
def test_1_create_a_list():
    l = [1,2,3,4,5]
    return l


# TODO Complete the function so it returns a list of numbers from 0 to 20
#  with both numbers 0 and 20 included in the list
def test_2_generate_a_list():
    l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    return l


# TODO Complete the function so it returns the product of all the numbers in
#  the list multiplied together
def test_3_product(list_1):
    s = 1
    for i in range(len(list_1)):
        s *= list_1[i]
    return s


# TODO Complete the function so it returns a list with all the elements from
#  list_1 followed by items in list_2
def test_4_combine_lists(list_1, list_2):
    l = list()
    for i in list_1:
        l.append(i)

    for i in list_2:
        l.append(i)
    return l

# ======================= DO NOT EDIT THE CODE BELOW =========================

class ListTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(5, len(test_1_create_a_list()))

    def test_2(self):
        generated_list = test_2_generate_a_list()

        self.assertEqual(21, len(generated_list))

        for index in range(21):
            self.assertEqual(index, generated_list[index])

    def test_3(self):
        test_list = [1, 5, -1, 2]
        self.assertEqual(-10, test_3_product(test_list))

        test_list = [91, 50, 120, 7, 0]
        self.assertEqual(0, test_3_product(test_list))

    def test_4(self):
        list_1 = ['Cody', 'Peter', 'Arnav']
        list_2 = ['Serena', 'Leslie', 'Irina']
        self.assertEqual(['Cody', 'Peter', 'Arnav', 'Serena', 'Leslie', 'Irina'], test_4_combine_lists(list_1, list_2))


if __name__ == '__main__':
    unittest.main()
