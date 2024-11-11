d = dict(key1=1, key2='hello', key3=10 + 5j)
print(d, id(d))
d['key4'] = '10.90'
print(d, id(d))
