
def print_values(values):
    print("start count")
    for i in values:
        print(i)
    print("stop count")

print_values(range(10))

# numbers
print(5)
print(8.2)
print(int(8.2))
print(int(8.7))
c1 = 3 + 4j
c2 = 8 - 2j
print(c1 + c2)

print("-----------------------------------------------------")

# text
a_string = "Hello world!"
print(a_string)
print(a_string == 'Hello world!')
print(a_string is 'Hello world!')
print('lo wo' in a_string)
print(a_string.title())
print(a_string.upper())
print(a_string.replace("o world!", " Yeah!!!"))
print(", ".join(["a", "b", "c", "d", "e"]))

print("-----------------------------------------------------")

# sequences
#  list
a_list = [1, 2, 3, 4, 5, ]
print(a_list)
first_3_numbers = a_list[:3]
print(first_3_numbers)
last_3_numbers = a_list[-3:]
print(last_3_numbers)
odd_num_from_3 = a_list[2::2]
print(odd_num_from_3)
print(a_list + [6, 7, 8, ])
print(a_list * 2)
print(3 in a_list)
#   tuple
a_tuple = ("a", 1, "b")
print(a_tuple)
#   range
r = range(2, 10, 2)
print(r)
for j in r:
    print(j)
#   set
print({2, 1, 2, 3, 1, 3, 4, })

print("-----------------------------------------------------")

# dictionaries
a_dict = {"a": "A", "b": "B", "c": "C", }
print(a_dict)
print('b' in a_dict)
print(a_dict.setdefault("d", "D"))
for k, v in a_dict.items():
    print(k + " -> " + v)

print("-----------------------------------------------------")


# miscellaneous
a = 5
b = 12
print("(" + str(a) + ", " + str(b) + ")")
a, b = b, a
print("(" + str(a) + ", " + str(b) + ")")

with open('data_source.txt', 'r') as f:
    print(f.readlines())
