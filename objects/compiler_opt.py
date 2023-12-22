# those resultants which is <20(the limit can be changed) chars is pre-calculated for optimization

def my_fun():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 11
    d = 'a quick brown fox' * 250
    e = ['a', 'c'] * 3  # won't get pre-calculated as it is a mutable object


print(my_fun.__code__.co_consts)


# the list gets changed to its counterpart immutable one -tuple
def list_change():
    for _ in [1, 2, 3]:
        pass


print(list_change.__code__.co_consts)


# set changes to its counterpart immutable one-frozenset
def set_change():
    for _ in {1, 2, 3}:
        pass


print(set_change.__code__.co_consts)
