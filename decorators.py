
class MyDecorator(object):

    def __init__(self, f):
        print("inside MyDecorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside MyDecorator.__call__()")


@MyDecorator
def a_function():
    print("inside a_function()")

print("Finished decorating a_function()")

a_function()


print("-----------------------------------------------------")


class EntryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)


@EntryExit
def func1():
    print("inside func1()")


@EntryExit
def func2():
    print("inside func2()")

func1()
func2()
