import sys

cases = int(sys.stdin.readline())

for case in range(cases):
	plays = (sys.stdin.readline()).split()
	point1 = 0
	point2 = 0

	for play in plays:

		if play[0] == "S" and play[1] == "P":
			point1 += 1
		elif play[0] == "P" and play[1] == "R":
			point1 += 1
		elif play[0] == "R" and play[1] == "S":
			point1 += 1

		elif play[1] == "S" and play[0] == "P":
			point2 += 1
		elif play[1] == "P" and play[0] == "R":
			point2 += 1
		elif play[1] == "R" and play[0] == "S":
			point2 += 1

	if point1 > point2:
		print "1", 
	else:
		print "2",