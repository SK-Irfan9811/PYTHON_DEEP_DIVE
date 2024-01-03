# the new physical lines are not going to convert to single logical line implicitly
# inline comments are not allowed in an explicit conversion
# need to use backslash to explicitly tell for continuing the flow


if 1 \
        and 2 \
        and 3:
    print("yahoo")
