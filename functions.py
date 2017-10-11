def a_function(a, b, c, d="DD", *k, **kw):
    print(a)
    print(b)
    print(c)
    print(d)
    print(k)
    print(kw)

kw = {'b': 'B', 'd': 'D', 'e': 'E', 'f': 'F', }

a_function(1, 2, 3, 4, 5, 6, 7, 8, 9)
a_function('A', c='C', **kw)
a_function('A', 'B', 'C')

