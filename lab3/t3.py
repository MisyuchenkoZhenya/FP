from functools import reduce

from pymonad.List import *
from pymonad.Reader import curry


#const variable not supported in python


#clear function
def add(x, y):
    return x + y


#first-ordered function
def test():
    print('Test')


#high-ordered function
def firstFunc():
    print("1")

def secondFunc():
    print("2")

def invoke(type, firstFunc, secondFunc):
    if type == '1':
        firstFunc()
    elif type == '2':
        secondFunc()


#curry-function
def curryFunc(f):
    return lambda a: lambda b: f(a, b)


#using of curry-function
def sum(a, b):
    return a + b

carriedSum = curryFunc(sum)
print(carriedSum(1)(2))


#memorization

addPrevious = lambda n: n + 10
addPrevious(10)# without memorize

def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate

@memoize
def addPrevious2(n):
    return n + 10

addPrevious2(10)
addPrevious2(10)# memorize


#lazy-counting of function
def fibonacci(n):
    fib1, fib2 = 0, 1
    for _ in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

for fib in fibonacci(20):
    print(fib, end=' ')
print()


#monade
def positive_and_negative(x):
    return List(x, -x)

positive_and_negative(9)

x = List(9)
x >> positive_and_negative

x = List(1, 2)
x >> positive_and_negative

@curry
def add_and_sub(x, y):
    return List(y + x, y - x)

List(2) >> positive_and_negative >> add_and_sub(3, 4)


#data structure
user = {
    'name': 'user',
    'email': 'user@mail.com',
    'prefs': {
        'languages': {
            'imperative': 'java',
            'functional': 'javascript'
        }
    }
};

#Inf data structure
#lambda
lambdaAdd = lambda x, y: x + y

#operation Map, Filter и Reduce.
arr = [1, 2, 3, 4, 5]
print(list(map(lambda item: item + 1, arr)))
print(list(filter(lambda item: item / 2 == 0, arr)))
print(reduce(lambda accumulator, currentValue: accumulator + currentValue, arr))
