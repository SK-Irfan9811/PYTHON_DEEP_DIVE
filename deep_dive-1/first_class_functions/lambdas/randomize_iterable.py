import random

f = lambda: random.randint(1, 10)

l = [x for x in range(f())]
# print(l)
# print(sorted(l, key=lambda x: random.random()))


# under the hood
def randomize(x):
    i = random.random()
    print(x,"-->", i)
    return i


# print(sorted(l, key=randomize))
