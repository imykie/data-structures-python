from __future__ import annotations

from typing import List


class SegmentTree:
    def __init__(self, nums: List[int], type: str = 'SUM') -> None:
        self.nums = nums
        self._n = len(nums)
        self._tree = [0] * (4 * self._n)
        self._type = type
        self._build(0, 0, self._n - 1)

    def _build(self, index: int, low: int, high: int) -> None:
        # if we can no longer break node into children
        if low == high:
            self._tree[index] = self.nums[low]
            return

        mid = low + (high - low) // 2
        self._build(2 * index + 1, low, mid)
        self._build(2 * index + 2, mid + 1, high)

        self._tree[index] = self._merge(
            self._tree[2 * index + 1], self._tree[2 * index + 2])

    def query(self, left: int, right: int) -> int:
        return self._query_helper(0, 0, self._n - 1, left, right)

    def _query_helper(self, index: int, low: int, high: int, left: int, right: int) -> int:
        # if completely outside of range
        if low > right or high < left:
            return 0

        # if completely in range
        if left <= low and right >= high:
            return self._tree[index]

        mid = low + (high - low) // 2

        # if the range is on the right (i.e after mid)
        if left > mid:
            return self._query_helper(2 * index + 2, mid + 1, high, left, right)
        # if the range is on the left (i.e before mid)
        elif right <= mid:
            return self._query_helper(2 * index + 1, low, mid, left, right)

        # else, split range
        left_query = self._query_helper(2 * index + 1, low, mid, left, right)
        right_query = self._query_helper(
            2 * index + 2, mid + 1, high, left, right)

        # merge left and right query
        return self._merge(left_query, right_query)

    def update(self, index: int, num: int) -> None:
        if index >= self._n:
            return
        return self._update_helper(0, 0, self._n - 1, index, num)

    def _update_helper(self, index: int, low: int, high: int, num_index: int, num: int) -> None:
        # update if leaf node
        if low == high:
            self._tree[index] = num
            return

        mid = low + (high - low) // 2
        # if the num index is on the right (i.e after mid)
        if num_index > mid:
            self._update_helper(2 * index + 2, mid + 1, high, num_index, num)
        # if the num index is on the left (i.e before mid)
        else:
            self._update_helper(2 * index + 1, low, mid, num_index, num)

        # update tree
        self._tree[index] = self._merge(
            self._tree[2 * index + 1], self._tree[2 * index + 2])

    def _merge(self, left: int, right: int):
        if self._type == 'MIN':
            return min(left, right)
        elif self._type == 'MAX':
            return max(left, right)
        return left + right

    def print_tree(self):
        print("nums: ", self.nums)
        print("tree: ", self._tree)


if __name__ == '__main__':
    sg = SegmentTree([3, 4, 5, 6], 'MIN')
    sg.print_tree()
    print(sg.query(1, 3))
    sg.update(2, 10)
    sg.print_tree()
    print(sg.query(1, 3))
