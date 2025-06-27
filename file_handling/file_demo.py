# f = open("sk.txt")
# content=f.read()
# print(f.writable(),f.mode)
import sys
import time
from html.parser import charref
from importlib.util import find_spec

# types of writing to a file.
# f = open("sk.txt", "w")
# f.write("SK\n")
# f.write("SK")
# f.write("SK")
# f.write("SK")
# f.write("")
# f.writelines(["IRFAN", "IRFAN", "IRFAN"])
# # f.writelines([2,3])
# f.close()

# reading a file
# cena = open("wwe.txt", "r")
# read_file = cena.read()  # moves cursor to the end of the file
# read_chars = cena.read(1000000)  # moves cursor to 10 chars forward
# read_one_line=cena.readline()
# read_all_lines=cena.readlines()


# print(f"Reading entire file\n - {read_file}")
# print(f"Reading n chars\n  {read_chars}")
# print(f"Reading one line\n  {read_one_line}")
# print(f"Reading one line\n  {read_all_lines}")

# reading from one file and writing to another file
# f1 = open("input.txt", "r")
# f2 = open("output.txt", "w")
# # f2.write(f1.read())
# # f2.write(f1.read(18))
# # f2.write(f1.readline())
# f1.read(10)
# print(f1.tell())
# f1.seek(f1.tell()+2)
# print(f1.tell())

# print no of lines words and characters in a file
#
# f = open("input.txt")
# lines_count = 0
# words_count = 0
# chars_count = 0
# for line in f:
#     lines_count += 1
#     words = line.split(" ")
#     words_count += len(words)
#     chars_count += len(line)
# print(f"Lines count - {lines_count} Words count -{words_count} Char count - {chars_count}")

# flush()
# f = open("log.txt", "a")
# for i in range(5):
#     f.write(f"Log entry {i+1}\n")
#     time.sleep(1)
# f.flush()  # Uncomment this to see immediate effect in `tail -f`

# multiple exceptions handling
# try:
#     print(10/0)
# except (ValueError) as msg:
#     print("got ur back - " , msg.__class__)
#
# finally:
#     print("I am always...")

try:
    print("hello")
    sys.exit(0)
except ZeroDivisionError:
    pass
else:
    pass
finally:
    print("Hurrah")

