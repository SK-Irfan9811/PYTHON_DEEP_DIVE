def outer():
    def inner():
        global n
        n = 100
        print(n)

    inner()


outer()
