import sys, math

cases = int(sys.stdin.readline())

for case in range(cases):
	number = (sys.stdin.readline()).split()
	number = map(int, number)
	suma = 0

	for i in [0, 1]:
		div = number[i] * 1.0 / 6
		div = div - math.floor(div)
		div = int(round(div*6 + 1))
		suma = suma + div

	print suma,