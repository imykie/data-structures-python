from LinkedList import SinglyLinkedList


class Deque:
    def __init__(self):
        self.__data = SinglyLinkedList()


    def append(self, x: int) -> None:
        self.__data.add_last(x)


    def prepend(self, x: int) -> None:
        self.__data.add_first(x)


    def pop(self) -> None:
        self.__data.remove_last()


    def popleft(self) -> None:
        self.__data.remove_first()


    def contains(self, x: int) -> bool:
        return self.__data.contains(x)


    def remove(self, x: int) -> None:
        self.__data.remove(x)


    def size(self) -> int:
        return self.__data.size


    def clear(self) -> None:
        self.__data.clear()

