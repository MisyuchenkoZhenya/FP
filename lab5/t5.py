import re
from functools import reduce

searchString = 'public class Person {private final String name; private final int age;}'

def f(mass, value):
    mass[value] = mass[value] + 1 if value in mass.keys() else 1

    return mass

result = reduce(lambda prev, nxt: f(prev, nxt),
    list(re.findall(r'[a-z]+', searchString.lower())),
    {}
)

print(result)
