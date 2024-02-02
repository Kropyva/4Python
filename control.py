import math

print('Enter two integer')

first = int(input('First value: '))
second = int(input('Second value: '))

absolute = abs(math.pow(first, 2) - math.pow(second, 2))
square = math.pow((first - second),2)

if absolute > square:
	print('Absolute value differece is bigger', absolute, '>', square)
else:
	print('Square difference is bigger', square, '>', absolute)