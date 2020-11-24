from LinkedList import SinglyLinkedList


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
    print(l.head.data, l.head.next.data)


if __name__ == '__main__':
    test()
