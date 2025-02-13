import timing

code = '[x for x in range(100_000)]'
timed = timing.timeit(code, repeats=10000)
print(timed.repeats, timed.elapsed, timed.average)
