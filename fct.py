"""sasasasaSA"""


def add(a, b):
    """Adds two numbers"""
    return a + b


def say_hello(first_name, last_name='', age=0):
    print(f"hello {first_name, last_name}. Your age is {age}")

def test_say_hello():
    say_hello('teo', 'andreea', '6')
    params1=['a','b', '65']
    say_hello(*params1)
    params2={'first_name':'a', 'last_name':'b', 'age':'6'}
    print(params2['fist_name'])
    say_hello(**params2)


def f():
    return 10, 20, 30, 40




if __name__ == '__main__':
    print(__doc__)
    print(add.__doc__)

    while True:
        x=int(input('x='))
        y=int(input('y='))
        print(f'x+y= {add(x,y,)}')
        if x == 0 and y == 0:
            break
