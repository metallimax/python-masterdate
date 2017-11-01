def a_function(a, b, c, d="DD", *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(args)
    print(kwargs)
    print("-----------")

a_function(1, 2, 3, 4, 5, 6, 7, 8, 9)
kw = {'b': 'B', 'd': 'D', 'e': 'E', 'f': 'F', }
a_function('A', c='C', **kw)
a_function('A', 'B', 'C')

