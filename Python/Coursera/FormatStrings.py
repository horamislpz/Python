
name = 'Horamis'
number = 3
print('Hello {}, your lucky number is {}.'.format(name, number))
#the variable is printed in the same order as input


name = 'Horamis'
number = 3
print('Hello {name}, your lucky number is {number}.'.format(name=name, number=number))
#the variable is printed in the same order as input


def to_celsius(x):
    return (x-32) * 5/9
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))