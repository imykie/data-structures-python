from LinkedList import SinglyLinkedList
from Stack import Stack, StackArr


def test():
    # print(f'Hi, {name}')
    l = SinglyLinkedList()
    l.add_first(1)
    l.add_first(2)
    print(l.size)
    l.remove(2)
    l.add_last(3)
    l.add_last(12)
    l.remove_at_position(0)
    l.insert(7,1)
    l.replace(20,0)
    l.display()
    l.insert(30, 2)
    print('')
    print(l.find(12))
    print(l.get(2))
    l.insert(21,2)
    l.display()
    print('')
    l.reverse()
    l.display()


if __name__ == '__main__':
    test()
