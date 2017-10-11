import time


def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b

for f in fib():
    print(f)
    time.sleep(2)
