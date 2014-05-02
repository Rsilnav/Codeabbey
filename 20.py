import sys

vowels = ["a","e","i","o","u","y"]
cases = int(sys.stdin.readline())

for i in range(cases):
	number = 0
	phrase = sys.stdin.readline().rstrip()
	
	for letter in phrase:
		if letter in vowels:
			number = number + 1

	print number,