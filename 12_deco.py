


def decorator_function(function):
    def wrapper_function(*args, **kwargs):
        print('inside function {}'.format(function.__name__))
        for e in args: print(e)
        return function(*args, **kwargs)
    return wrapper_function

@decorator_function
def add(a,b):
    print('result is: ')
    return a+b

@decorator_function
def sum(a,b,c,d,e,f):
    print('result is :')
    return a+b+c+d+e+f


print(add(7,8))
print(sum(1,2,3,4,5,6))

