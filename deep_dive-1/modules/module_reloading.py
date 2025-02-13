import os.path
import sys


def create_module(file_name, **kwargs):
    mod_name = f"{file_name}.py"
    file_rel_path = mod_name
    file_abs_path = os.path.abspath(file_rel_path)

    with open(file_abs_path, 'w') as f:
        f.write(f"#{file_name}.py is created\n")
        f.write(f"print('{file_name} is running')\n")
        f.write("def print_values():\n")
        for k, v in kwargs.items():
            f.write(f"\tprint('{str(k)}','{str(v)}')\n")


create_module("test", name="Irfan", age=22)

import test

print(id(test))
test.print_values()
create_module("test", name="Irfan", age=23, fav="blue")
import test

print(id(test))
test.print_values()

# one way to get the latest changes and reload module is deleteing the label of test in sys.modules and in global name space
print("test" in globals())
print("test" in sys.modules)
del sys.modules["test"]
print("test" in globals())
print("test" in sys.modules)
import test  # load the latest code and replaces the existing test label with the latest ref of test code

test.print_values()
