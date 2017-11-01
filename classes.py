
class Person(object):
    some_attribute = "value"

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def inc_age(self):
        self.age += 1

    def __repr__(self):
        return "%s %s: %d" % (self.firstname, self.lastname, self.age, )

    def __getattr__(self, item):
        if item == "misc":
            print("**Getting misc YOLO**")
            return "YOLO!"
        else:
            print("**Getting %s**" % (item, ))
            return getattr(self, item)

    def __getitem__(self, item):
        if item == 0:
            return self.firstname
        elif item == 1:
            return self.lastname
        elif item == 3:
            return self.age

    def __call__(self, *args, **kwargs):
        print("Trying to call an object instance")
        print(args)
        print(kwargs)

m = Person("Maxime", "DELRIEU", 39)
m.inc_age()
print(m)
m.dynattr = "Hey There!"
print(m.age)
print(m.misc)
print(m[0])
print(m[1])
print(m[2])
print(m[3])
a = (4, 5)
m(1, 2, 3, *a)


# resolution order (linearization algorithm)
class Adam(object): pass
class Eve(object): pass
class Ramon(Adam, Eve): pass
class Gayle(Adam, Eve): pass
class Raymond(Ramon, Gayle): pass
class Dennis(Adam, Eve): pass
class Sharon(Adam, Eve): pass
class Rachel(Dennis, Sharon): pass
class Matthew(Raymond, Rachel): pass

help(Matthew)

print("-----------------------------------------------------")


# dependency injection
class DoughFactory(object):

    def get_dough(self):
        return 'insecticide treated wheat dough'


class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        print('Getting dough')
        dough = super().get_dough()
        print('Making pie with %s' % dough)
        for topping in toppings:
            print('Adding: %s' % topping)

Pizza().order_pizza('Pepperoni', 'Bell Pepper')

print("-----------------------------------------------------")


class OrganicDoughFactory(DoughFactory):

    def get_dough(self):
        return 'pure untreated wheat dough'


class OrganicPizza(Pizza, OrganicDoughFactory):
    pass

help(OrganicPizza)

print("-----------------------------------------------------")

OrganicPizza().order_pizza('Sausage', 'Mushroom')
