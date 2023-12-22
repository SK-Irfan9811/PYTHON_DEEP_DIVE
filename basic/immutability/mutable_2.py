def process(lst):
    print("initial id: ", id(lst))
    lst.append(200)
    print("initial id: ", id(lst))


ll = [1, 2, 3, 4]
print("original id", id(ll))
process(ll)
print("final id", id(ll))

a = [9, 8, 7]
b = [9, 8, 7]
print(id(a), id(b))
# for mutable objects addresses will be different always
