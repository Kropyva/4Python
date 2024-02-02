import heapq

arr = [5, 3, -7, -8, 5, 0, 3, 1, -4, 1, 3, -6, 16, 9, 0, 6, 1, 8, 4, 4, -1, 1, 12, 13, 10]
max_values = heapq.nlargest(2, arr)
idxs = [arr.index(value) for value in max_values]
idxs.sort()

count = 0
for idx, element in enumerate(arr):
	if idxs[0] < idx < idxs[1] and element % 2 == 0:
		count += 1
		print(f"{element}!", end=" ")
	else:
		print(f"{element}{'*' if idx in idxs else ''}", end=" ")

print(f"\nCount of even numbers between two maximum values: {count}")