n = int(input())
series = [3,5,7]
for j in range(3,n):
	int_term = series[j-3] + series[j-2] - series[j-1]
	series.append(int_term)
print(*series)    # here * is used to remove spacing and brackets