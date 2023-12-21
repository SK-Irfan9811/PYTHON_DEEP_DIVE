class A:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print("A's eq method")
        if isinstance(other, A):
            return self.val == other.val
        return NotImplemented


class B:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print("B's eq method")
        if hasattr(other, 'val'):
            return other.val == self.val
        return NotImplemented


a = A(1)
b = B(1)
print("from a", a == b)
print("from b", b == a)
