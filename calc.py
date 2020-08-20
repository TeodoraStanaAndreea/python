import math

def add(a, b):
    return a+b

def subs(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def root(a):
    return math.sqrt(a)

def square(a):
    return a*a

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)



if __name__ == '__main__':
    while True:
        a=int(input('a='))
        b=int(input('b='))
        print(f'add {a} and {b}={add(a,b)}')
        print(f'substract {a} and {b}={subs(a,b)}')
        print(f'multiply {a} and {b}={multiply(a,b)}')
        print(f'divide {a} and {b}={divide(a,b)}')
        print(f'root {a} is ={root(a)}')
        print(f'square {a} is ={square(a)}')
        print(f'sin {a} is ={sin(a)}')
        print(f'cos {a} is ={cos(a)}')
        if a==0 and b==0:
            break

