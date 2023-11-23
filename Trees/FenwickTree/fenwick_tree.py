class FenwickTree:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr
        self.__n = len(arr)
        self.__tree = [0] * (self.__n + 1)
        self.__build()


    def __build(self):
        self.__tree = [0] + self.arr
        for i in range(1, self.__n):
            p = i + self.__lowbit(i)
            if p < self.__n:
                self.__tree[p] = self.__tree[p] + self.__tree[i]


    def __add(self, idx: int, val: int):
        while idx < self.__n:
            self.__tree[idx] += val
            idx += self.__lowbit(idx)


    def __sum(self, idx: int):
        total = 0
        while idx > 0:
            total += self.__tree[idx]
            idx -= self.__lowbit(idx)

        return total
    

    def update(self, idx: int, val: int):
        delta = val - self.arr[idx]
        self.arr[idx] = val
        self.__add(idx + 1, delta)

        
    def query(self, left: int, right: int):
        return self.__sum(right + 1) - self.__sum(left)

    
    def __lowbit(self, x: int):
        return x & -x
    

    def __str__(self) -> str:
        return f"BIT: {self.__tree} \nArr: {self.arr}"
