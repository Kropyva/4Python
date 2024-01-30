import random

max_size = 42
one_nine = int(max_size * 0.2)
zeros = int(max_size * 0.2)
array = [None] * max_size

for i in range(max_size):
	if one_nine:
		array[i] = random.randint(1, 9)
		one_nine -= 1
	elif zeros:
		array[i] = 0
		zeros -= 1
	else:
		if (random.randint(0, 1)):
			array[i] = random.randint(10, 99)
		else:
			array[i] = random.randint(-99, -1)

with open('input.txt', 'w') as file:
	random.shuffle(array)
	file.write(str(array)[1:-1])
