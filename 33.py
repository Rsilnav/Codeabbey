import sys

letters = (sys.stdin.readline().rstrip()).split()

letters = map(int, letters)

result = ""

for l in letters:
	binary = '{0:08b}'.format(l)
	binary = '0' + binary[1:]

	result = result + chr(int(binary, 2))

print result