n = int(input())
result = []
for i in range(1, n+1):
	sum_power = sum([i**j for j in range(1, i+1)])
	result.append(sum_power)
print(*result)