import sys

words = (sys.stdin.readline()).split()

passphrase = []

for word in words:
	if word not in passphrase:
		if words.count(word) > 1:
			passphrase.append(word)

passphrase.sort()

print " ".join(passphrase)