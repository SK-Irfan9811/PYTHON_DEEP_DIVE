# physical multiple new lines gets converted to logical single line

# list
a = ["egg",  # non-veg
     "chapathi",  # veg
     ]
print(a)

# list
a = ("hen",  # bird
     "crocodile",  # reptile
     )
print(a)

# dict
a = {"one": 1,  # one:1
     "two": 2
     }
print(a)


# In functions
def my_func(p,  # first param
            q,  # second param
            ):
    print(p, q)


my_func("JohnCena",  # wrestler
        "Irfan"  # pro-wrestler
        )
