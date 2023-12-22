a = "my name is s_k"
b = "my name is s_k"
print(a is b)

a = 'hello world'
b = 'hello world'
print(a is b)  # could be false as it is not an identifier

# inorder to get interned the strings must be in identifier format
a = 'hello_world'
b = 'hello_world'
print(a is b)  # true always as value is identifier satisfying


