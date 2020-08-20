from os import system
system('clear')
    while True:
        name= input('Enter your name: ')
        if name=='' or name is None:
            print ('goodbye')
        break
    print(f'Hello {name}')

