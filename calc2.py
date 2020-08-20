import math


def add(l):
    return sum([int(x) for x in l])

def sub(l):
    return int(l[0])-sum([int(x) for x in l[1:]])

def prod(l):
    return math.prod([int(x) for x in l])

def invalid(l):
    return 'Invalid function'


if __name__ =='__main__':
    ops={'add':add, 'sub':sub, 'prod':prod}
    while True:
        line=input('Expression: ')
        if line == 'end':
            break

        tokens=line.lower().split()
        f=ops.get(tokens[0]) or invalid
        print(f'{f(tokens[1:])}')
