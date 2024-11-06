import time


class ThreeSum:
    def __init__(self, arr):
        self.arr = arr

    def find_triplets_with_sum0(self):
        count = 0
        for i in range(len(self.arr)):
            for j in range(i + 1, len(self.arr)):
                for k in range(j + 1, len(self.arr)):
                    if self.arr[i] + self.arr[j] + self.arr[k] == 0:
                        count += 1
        return count


start = time.time()
t = ThreeSum([30, -40, -20, -10, 40, 0, 10, 5] * 10)
print(t.find_triplets_with_sum0())
end = time.time()
print(end - start)

start = time.time()
t = ThreeSum([30, -40, -20, -10, 40, 0, 10, 5] * 50)
print(t.find_triplets_with_sum0())
end = time.time()
print(end - start)

start = time.time()
t = ThreeSum([30, -40, -20, -10, 40, 0, 10, 5] * 100)
print(t.find_triplets_with_sum0())
end = time.time()
print(end - start)

start = time.time()
t = ThreeSum([30, -40, -20, -10, 40, 0, 10, 5] * 500)
print(t.find_triplets_with_sum0())
end = time.time()
print(end - start)
