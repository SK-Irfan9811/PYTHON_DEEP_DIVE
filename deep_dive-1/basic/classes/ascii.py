import string

print(','.join(string.ascii_uppercase))
# ord() and chr()
for i in range(ord('a'), ord('z') + 1):
    print(i, end="")

for i in range(259):
    print(chr(i), i, end="")
print()
print("Irfan {} cricket".format(chr(10084)))
