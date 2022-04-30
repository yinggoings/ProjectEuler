i = 1
j = 2
sum = j
while j < 4000000:
	pasti = i
	i = j # i = 2
	j += pasti # j = 3
	if j % 2 == 0:
		sum+=j
print(sum)

