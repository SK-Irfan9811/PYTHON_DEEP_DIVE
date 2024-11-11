# range() is an iterable sequence
for i in range(5):
    print(i, end="")

for a, b in [(2, 4), (3, 9), (4, 16)]:
    print("square of {0} is {1}".format(a, b))  # tuple unpacking

for i in range(1, 10, 2):
    if i % 2 == 0:
        print("even found", i)
        break
else:
    print("no even numbers found")

for i in range(5):
    print("---------------------")
    try:
        5 / (i - 3)
    except ZeroDivisionError:
        print("division by zero")
        continue
    finally:
        print("always executes")
    print(i)

for idx, char in enumerate("Irfan"):
    print(idx, char)
