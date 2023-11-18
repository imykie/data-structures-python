class MergeSort:
    def __init__(self, arr) -> None:
        self.arr = arr
    

    def _merge(self, left: int, mid: int, right: int):
        n1 = mid - left + 1
        n2 = right - mid

        left_temp_arr = [0] * n1
        right_temp_arr = [0] * n1

        for i in range(n1):
            left_temp_arr[i] = self.arr[left + i]
        for i in range(n2):
            right_temp_arr[i] = self.arr[mid + 1 + i]

        i, j, k = 0, 0, left

        while i < n1 and j < n2:
            if left_temp_arr[i] < right_temp_arr[j]:
                self.arr[k] = left_temp_arr[i]
                i += 1
            else:
                self.arr[k] = right_temp_arr[j]
                j += 1
            k += 1

        while i < n1:
            self.arr[k] = left_temp_arr[i]
            i += 1
            k += 1

        while j < n2:
            self.arr[k] = right_temp_arr[j]
            j += 1
            k += 1
        

    def _merge_sort(self, left: int, right: int):
        if left >= right:
            return
        
        mid = (left + right) // 2
        # divide into two halves and sort recursively
        self._merge_sort(left, mid)
        self._merge_sort(mid + 1, right)
        # merge the sorted halves
        self._merge(left, mid, right)


    def sort(self):
        self._merge_sort(0, len(self.arr) - 1)
        return self.arr

