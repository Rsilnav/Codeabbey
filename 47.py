import sys

cases, shift = (sys.stdin.readline().rstrip()).split()
cases = int(cases)
shift = int(shift)
result = []

for case in range(cases):
	decipher = ""
	phrase = sys.stdin.readline().rstrip()

	for l in phrase:
		if l.isalpha():
			if ord(l)-shift < 65:
				decipher = decipher + chr(ord(l)+26-shift)
			else:
				decipher = decipher + chr(ord(l)-shift)
		else:
			decipher = decipher + l
	result.append(decipher)

print " ".join(result)