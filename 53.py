import sys

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

cases = int(sys.stdin.readline())

for case in range(cases):
	king, queen = (sys.stdin.readline()).split()

	if king[1] == queen[1]:
		print "Y",
	elif king[0] == queen[0]:
		print "Y",
	elif abs(int(king[1]) - int(queen[1])) == abs( letters.index(king[0])+1 - letters.index(queen[0])+1):
		print "Y",
	else:
		print abs(int(king[1]) - int(queen[1])), abs( letters.index(king[0])+1 - letters.index(queen[0])+1), "N",