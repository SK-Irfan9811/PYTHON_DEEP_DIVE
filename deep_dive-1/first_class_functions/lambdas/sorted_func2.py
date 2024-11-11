f = lambda tpl: tpl[1]
d = {1: 'one', 2: 'two', 3: 'three'}  # d is in global scope, no matter what order is in
dd = sorted(d.items(), key=f)
print(dd)
