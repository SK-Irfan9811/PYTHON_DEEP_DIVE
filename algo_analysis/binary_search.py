class BinarySearch:
    def __init__(self, arr):
        self.arr = sorted(arr)

    def find(self, key: int):
        low = 0
        high = len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if key > self.arr[mid]:
                low = mid + 1
            elif key < self.arr[mid]:
                high = mid - 1
            else:
                return True
        return False


b = BinarySearch([2, 3, 4, 5, 1, 8, 9, 0, 1])
print(b.find(7))
