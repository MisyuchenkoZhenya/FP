
# 4.1
def modificate(func, param):
    return func(param)

print('FIRST')
print(modificate(lambda x: x*x, 10))
print(modificate(lambda x: x*x*x, 20))
print(modificate(lambda x: -x, 30))


# 4.2
def filterFunc(collection, func):
    return list(filter(lambda item: func(item), collection))

print('\nSECOND')
print(filterFunc([1, 4, 7, 15, 24], lambda x: x < 10))


# 4.3
def compose2(f, g):
    return lambda x: f(g(x))

mapFunc = lambda cb: lambda arr: list(map(cb, arr))
filterCompose = lambda cb: lambda arr: list(filter(cb, arr))

users = [
    {'prop': 'First', 'otherProp': 10},
    {'prop': 'Second', 'otherProp': 20},
    {'prop': 'Third', 'otherProp': 30}
]

print('\nTHIRD')
comp = compose2(mapFunc(lambda u: u['prop']), filterCompose(lambda u: u['otherProp'] >= 18))
print(comp(users))
