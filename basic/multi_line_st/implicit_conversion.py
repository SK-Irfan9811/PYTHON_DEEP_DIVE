# implicit conversion is supported by [],(),{} and func args and params


# sequences
_list = [1,  # this physical new line is implicitly ignored and
         2,  # continue with next line to single logical line
         3]

_tuple = (1,
          2,
          3)

_set = {1,
        2,
        3}

_dict = {1: "one",
         2: "two",
         3: "three"}

print(_list, _tuple, _set, _dict)


# functions
def my_fun(name,  # must be a str
           age,  # must be integer between 0 and 100
           children):
    print(name, "'s age is", age, "and has", children, "children")


my_fun("Cena",
       45,
       4)
