#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
print('This program give you the posibility to do simple mathematical operations')
print('Please select one of the following:  1 Add, 2 Product, 3 Power, 4 Which bigger')
n=int(input())
x=int(input('The value X is:    '))
y=int(input('The value Y is:    '))
if n == 1:
        print('Add:     ',x+y)
elif 2 == n:
        print('Product:     ', x*y)
elif n == 3:
        print('Power:       ',x**y)
elif n == 4:
    if x>y:
            print('The first is bigger')
    elif x<y:
            print('The second is bigger')
    else:
            print('No case')
else:
    print('Choose an option')
