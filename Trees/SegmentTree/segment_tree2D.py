class SegmentTree2D:
    def __init__(self, nums: list[list[int]]):
        self.nums = nums
        self.rows = len(self.nums)
        self.cols = len(self.nums[0])
        self.tree = [[0] * (self.cols * 4) for _ in range(self.rows * 4)]
        self._build2D(1, 0, self.rows - 1)
        

    def _build(self, tree: list[int], arr: list[int], tree_idx: int, low: int, high: int) -> None:
        if low == high:
            tree[tree_idx] = arr[low]
            return
        
        mid = self._get_mid(low, high)
        self._build(tree, arr, 2 * tree_idx, low, mid)
        self._build(tree, arr, 2 * tree_idx + 1, mid + 1, high)
        # merge children to parent
        tree[tree_idx] = self._merge(tree[2 * tree_idx], tree[2 * tree_idx + 1])


    def _build2D(self, tree_idx: int, low: int, high: int) -> None:
        if low == high:
            self._build(self.tree[tree_idx], self.nums[low], 1, 0, self.cols - 1)
            return
        
        mid = self._get_mid(low, high)
        self._build2D(2 * tree_idx, low, mid)
        self._build2D(2 * tree_idx + 1, mid + 1, high)
        # merge left and right child
        for i in range(len(self.tree[tree_idx])):
            self.tree[tree_idx][i] = self._merge(self.tree[2 * tree_idx][i], self.tree[2 * tree_idx + 1][i])


    def query(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return self._query2D(1, 0, self.rows - 1, x1, y1, x2, y2)
    

    def _query(self, tree: list[int], tree_idx: int, low: int, high: int, left: int, right: int) -> int:
        # out or range
        if low > right or high < left:
            return 0
        
        # completely in range
        if low >= left and high <= right:
            return tree[tree_idx]
        
        mid = self._get_mid(low, high)
        left_query = self._query(tree, 2 * tree_idx, low, mid, left, right)
        right_query = self._query(tree, 2 * tree_idx + 1, mid + 1, high, left, right)

        # range is on the right
        if left > mid:
            return right_query
        # range is on the right
        elif right <= mid:
            return left_query
        
        # split range
        return self._merge(left_query, right_query)
    
    
    def _query2D(self, tree_idx: int, low: int, high: int, x1: int, y1: int, x2: int, y2: int):
        # out of range
        if (low > x2 or high < x1):
            return 0
        
        # completely in range
        if low >= x1 and high <= x2:
            return self._query(self.tree[tree_idx], 1, 0, self.cols - 1, y1, y2)
        
        mid = self._get_mid(low, high)
        left_query = self._query2D(2 * tree_idx, low, mid, x1, y1, x2, y2)
        right_query = self._query2D(2 * tree_idx + 1, mid + 1, high, x1, y1, x2, y2)

        # range is on the right
        if x1 > mid:
            return right_query
        # range is on the left
        elif x2 <= mid:
            return left_query
        
        # split range
        return self._merge(left_query, right_query)
    
    def update(self, x: int, y: int, val: int) -> int:
        return self._update2D(1, 0, self.rows - 1, x, y, val)
    

    def _update(self, tree: list[int], tree_idx: int, low: int, high: int, arr_idx: int, val: int) -> None:
        if low == high:
            tree[tree_idx] = val
            return
        
        mid = self._get_mid(low, high)
        if arr_idx > mid:
            self._update(tree, 2 * tree_idx + 1, mid + 1, high, arr_idx, val)
        elif arr_idx <= mid:
            self._update(tree, 2 * tree_idx, low, mid, arr_idx, val)

        tree[tree_idx] = self._merge(tree[2 * tree_idx], tree[2 * tree_idx + 1])


    def _update2D(self, tree_idx: int, low: int, high: int, x: int, y: int, val: int) -> None:
        if low == high:
            return self._update(self.tree[tree_idx], 1, 0, self.cols - 1, y, val)
        
        mid = self._get_mid(low, high)
        if x > mid:
            self._update2D(2 * tree_idx + 1, mid + 1, high, x, y, val)
        elif x <= mid:
            self._update2D(2 * tree_idx, low, mid, x, y, val)

        for i in range(len(self.tree[tree_idx])):
            self.tree[tree_idx][i] = self._merge(self.tree[2 * tree_idx][i], self.tree[2 * tree_idx + 1][i])

    
    def _get_mid(self, low: int, high: int):
        return low + (high - low) // 2
            
    
    def _merge(self, x: int, y: int):
        return x + y
    

    def __str__(self) -> str:
        return f"{self.tree}"

