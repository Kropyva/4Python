import matplotlib.pyplot as plot

try:
	with open('input.txt', 'r') as file:
		array = [int(x) for line in file for x in line.split(',')]
		print(array)
except Exception as e:
	print(str(e))

max_value = max(array)
zeros = sum(1 for x in array if x == 0)
one_nine = sum(1 for x in array[array.index(max_value):] if 1 <= x <= 9)

print("Max:", max_value)
print("Count of zeros:", zeros)
print("Count of numbers from one to nine:", one_nine)

array.sort()
zero = array.index(0)
twenty_percent = int(len(array) * 0.2)

negatives = array[:zero]
zeros = array[zero:zero + twenty_percent]
one_nine = array[zero + twenty_percent: zero + twenty_percent * 2]
remainder = array[zero + twenty_percent * 2:]

categories = ['From one to nine', 'Zeros', 'Remainder']
values = [len(one_nine), len(zeros), len(negatives + remainder)]

plot.figure(figsize=(8, 6))
ax = plot.gca()

bars = ax.bar(categories, values, color=['b', 'g', 'r'])
plot.xlabel('Categories')
plot.ylabel('Counts')
plot.title('Chart')
plot.annotate(f'Max: {max_value}', xy=(categories[2], len(negatives + remainder) - 1), ha='center')

plot.tight_layout()
plot.show()

array.clear()
array = one_nine + zeros + negatives + remainder
print(array)