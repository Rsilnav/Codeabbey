import sys

cases = int(sys.stdin.readline())

for case in range(cases):
	number, phrase = (sys.stdin.readline()).split()
	number = int(number)

	print phrase[number:]+phrase[:number],