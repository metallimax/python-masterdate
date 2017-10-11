
print('%s has %03d quote types.' % ("Python", 2, ))

print('%(language)s has %(number)03d quote types.' % {"number": 2, 'language': "Python", })

print('Hello \n world!')
print(r'Hello \n world!')

import re

r = re.compile(r'(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})')
m = r.match("2017-10-11")
print(m)
g = m.groupdict()
print(g)
print("%(day)s/%(month)s/%(year)s" % g)
m = r.match("do this string match?")
print(m is None)
