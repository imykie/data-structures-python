from LinkedList import SinglyLinkedList
from Stack import Stack, StackArr
from Trees import BinarySearchTree, AVLTree


def test():
    # print(f'Hi, {name}')

    # t = BinarySearchTree()
    # t.insert(20)
    # t.insert(30)
    # t.insert(45)
    # t.insert(55)
    # print(t.root.data, t.root.right.data, t.root.right.right.data, t.root.right.right.right.data)
    # t.print_tree()
    # t.invert()
    # print()
    # t.print_tree()
    # t.remove(5)
    # t.remove(25)
    # t.remove(35)
    # t.remove(25)
    # print(t.contains(50))
    # t.print_tree()
    # a = t.predecessor_alt(t.root, 0, 15)
    # # a = t.predecessor(5)
    # print(a.data)
    # t.preorder()
    # print()
    # t.inorder()
    # print()
    # t.postorder()
    # t.invert()
    # print()
    # t.print_tree()

    a = AVLTree()
    a.insert(20)
    a.insert(30)
    a.insert(40)
    a.insert(50)
    a.insert(60)

    a.insert(70)

    a.insert(80)

    print(a.root.balance, a.root.right.balance)
    # print(a.find(50).parent.data, a.find(80).parent.data)
    # print(a.root.right.parent.data, a.root.right.right.parent.data, a.root.right.right.right.parent.data, a.root.right.right.right.right.parent.data)
    # a.insert(40)
    # a.insert(45)
    # a.insert(50)
    # a.insert(10)
    # a.insert(20)
    # a.insert(5)
    a.print_tree()


if __name__ == '__main__':
    test()
