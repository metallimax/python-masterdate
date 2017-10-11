from mymodule import *

print(myfirstfeature)

try:
    print(mysecondfeature)
except NameError:
    from mymodule import mysecondfeature

print(mysecondfeature)

print(myfirstfeature.first_feature_func())
print(mysecondfeature.second_feature_func())
