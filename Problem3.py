n = 600851475143
nn = n
pfs = set()
while n != 1:
	for i in range(2,nn):
		if n%i == 0:
			n = int(n/i)
			pfs.add(i)
			break
print(max(pfs))


