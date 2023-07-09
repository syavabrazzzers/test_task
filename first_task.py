count = int(input())
numbers = []
for i in range(1, count+1):
    for j in range(i):
        numbers.append(i)
print(numbers)
