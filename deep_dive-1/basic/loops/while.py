# else will execute only if while gets exhausted but not in abrupt termination
# but due to a break statement
lst = [1, 2, 3, 0]
val = 10
idx = 0
while idx < len(lst):
    if lst[idx] == val:
        break
    idx += 1
else:
    lst.append(val)
    print("else block")
print(lst)
