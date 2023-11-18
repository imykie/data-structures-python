from LinkedList import SinglyLinkedList
from Stack import Stack, StackArr
from Trees import BinarySearchTree, AVLTree
from Sorts import MergeSort


def test():
    # print(f'Hi, {name}')

    # t = BinarySearchTree()
    # t.insert(20)
    # t.insert(30)
    # t.insert(23)
    # t.insert(21)
    # t.insert(55)
    # t.insert(18)
    # t.insert(15)
    # # # t.insert(19)
    # # t.insert(21)
    # # # print(t.root.data, t.root.right.data, t.root.right.right.data, t.root.right.right.right.data)
    # # # print(t.root.right.left.data)
    # t.print_tree()
    # t.remove(20)
    # print(t.minimum(t.root.right).data)
    # t.print_tree()

    a = AVLTree()
    a.insert(130)
    a.print_tree()
    a.insert(50)
    a.print_tree()
    a.insert(95)
    a.print_tree()
    a.insert(150)
    a.print_tree()
    a.insert(180)
    a.print_tree()
    a.insert(20)
    a.print_tree()
    a.insert(100)
    a.print_tree()
    a.insert(40)
    a.print_tree()
    a.insert(60)
    # a.insert(120)
    a.print_tree()
    a.delete(95)
    a.print_tree()
    a.delete(40)
    a.print_tree()
    a.delete(100)
    a.print_tree()
    # # a.delete(a.root, 50)
    # a.print_tree()
    #
    # a.inorder()
    #
    # t = a.get(40)
    # print(t.data)
    # print(t.parent.data, t.parent.right.data, t.parent.parent.data, t.parent.parent.left.data)

    # print(a.root.balance, a.root.right.balance)
    # print(a.find(50).parent.data, a.find(80).parent.data)
    # print(a.root.right.parent.data, a.root.right.right.parent.data, a.root.right.right.right.parent.data, a.root.right.right.right.right.parent.data)

    l = [477, 1193, 2130, 398, 1393, 946, 422, 1381, 1767, 830, 570, 1085, 741, 598, 1658, 1801, 487, 1921, 1918, 258, 135, 975, 1870]

    # for i in l:
    #     a.insert(i)
    # a.print_tree()


if __name__ == '__main__':

    # # bubble sort
    a = [5, 1, 4, 2, 8]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    # print(a)

    # # insertion sort
    # a = [5, 1, 4, 2, 8]
    # n = len(a)
    # for i in range(1, n):
    #     key = a[i]
    #     j = i - 1

    #     while j >= 0 and key < a[j]:
    #         a[j + 1] = a[j]
    #         j -= 1
    #     a[j + 1] = key

    # print(a)

    # # selection sort - look for minimum and put it first
    # a = [5, 1, 4, 2, 8]
    # n = len(a)

    # for i in range(n):
    #     minimum = i

    #     for j in range(i + 1, n):
    #         if a[minimum] > a[j]:
    #             minimum = j

    #     # swap minimum
    #     a[i], a[minimum] = a[minimum], a[i]

    # print(a)
    # m = MergeSort(a)
    # print("merge_sort", m.sort())
        

    # print([i for i in range(35, 61)])

    # test()

