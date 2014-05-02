import sys

cases = int(sys.stdin.readline())

for case in range(cases):
	phrase = sys.stdin.readline().rstrip()
	letters = ""

	for letter in phrase:
		if letter.isalpha():
			letters = letters + letter.lower()

	if letters == letters[::-1]:
		print "Y",
	else:
		print "N",