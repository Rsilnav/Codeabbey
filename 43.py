import sys

cases = int(sys.stdin.readline())

for case in range(cases):
	number = float(sys.stdin.readline())
	print int(round(number*6 + 1)),