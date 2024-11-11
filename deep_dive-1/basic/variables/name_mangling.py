class A:
    _var = 10

    def get_var(self):
        return A._var


class B(A):
    __var = 20

    def get_var(self):
        return self.__var


if __name__ == '__main__':
    a = A()
    b = B()
    print(b._B__var, 'from direct access-b')  # name mangling, internally python stores that var in that form
    print(A._var, 'from direct access-a')  # normal accessing
    print(b.get_var(), "from method")
