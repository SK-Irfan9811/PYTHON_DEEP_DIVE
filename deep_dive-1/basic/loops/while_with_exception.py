a = 0
b = 10
while a < 4:
    a += 1
    b -= 1
    try:
        a / b
        print(a, b)
    except ZeroDivisionError:
        print("{0},{1} are not divisible".format(a, b))
        break
    finally:
        print("always executes..")
else:
    print("code ran without break st")
