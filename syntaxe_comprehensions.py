
# regular loop
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# map + lambda
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# list comprehension
squares = [x**2 for x in range(10)]
print(squares)

print("-----------------------------------------------------")

# set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

print("-----------------------------------------------------")

# dict comprehension
d = {n: n**2 for n in range(10)}
print (d)

print("-----------------------------------------------------")

# generator comprehensions
s = sum(x*x for x in range(10))
print(s)
