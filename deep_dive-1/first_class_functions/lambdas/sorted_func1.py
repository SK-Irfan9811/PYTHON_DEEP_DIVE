# help(sorted)
print(sorted([3, 4, 5, 6, 7, 8, 6]))
print(sorted(['a', 'b', 'z'], reverse=True))
print(sorted(['a', 'C', 'D', 'b'], key=lambda x: x.lower()))  # case -insensitive
# sorting the complex numbers
c = [1 + 1j, 10 - 3j, 5 - 8j, 0 + 0j]
# print(sorted(c)) we can't compare coplex numbers
print(sorted(c, key=lambda x: ((x.real) ** 2 + (x.imag) ** 2), reverse=False))

alphas = ['Irfan', 'SK_Irfan', 'Goutaam', 'Sairam']
print(sorted(alphas, key=lambda x: (x[-1])))  # tiebreaker is based on their position in list

