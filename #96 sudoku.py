#return id of square
def nodouble(rowandcolume, puzzle):
	row = rowandcolume[0]
	colume = rowandcolume[1]
	checklist = []
	#check in the same row
	for i in puzzle[row]:
		if i not in checklist and i != 0:
			checklist.append(i)
		elif i == 0:
			continue
		else:
			return False
	#check in same colume
	checklist = []
	for j in range(9):
		if puzzle[j][colume] in checklist:
			return False
		elif puzzle[j][colume] != 0:
			checklist.append(puzzle[j][colume])
	checklist = []
	if row < 3:
		row = 0
	elif row < 6:
		row = 3
	else:
		row = 6
	if colume < 3:
		colume = 0
	elif colume < 6:
		colume = 3
	else:
		colume = 6
	for a in range(3):
		for b in range(3):
			if puzzle[row +a][colume +b] in checklist:
				return False
			elif puzzle[row +a][colume +b] != 0:
				checklist.append(puzzle[row +a][colume +b])
	return True
# find empty location return in list 
# list format [[2,3],[2,4]]
def empty(puzzle):
	emptylist = []
	for row in range(9):
		for colume in range(9):
			if puzzle[row][colume] == 0:
				emptylist.append([row,colume])
	return emptylist
def solve(puzzle):
	emptylist = empty(puzzle)
	working, test = 0,0
	while working < len(emptylist):
		inrow = emptylist[working][0]

		incol = emptylist[working][1]
		workingno = puzzle[inrow][incol]
		while workingno < 10:
			workingno += 1
			puzzle[inrow][incol] = workingno
			if nodouble(emptylist[working], puzzle):
				break
		if workingno == 10:
			working -=1
			puzzle[inrow][incol] = 0
			#print("maxed")
		else:
			puzzle[inrow][incol] = workingno
			working += 1
		test += 1
	return puzzle
def return3(sudoku):
	solved = solve(sudoku)
	return solved[0][0] * 100 + solved[0][1] *10 + solved[0][2]
f = open('p096_sudoku.txt', 'r')
data = f.readlines()
total = 0
for xx in range(50):
	sudoku = []
	for i in range(1+xx*10,1+xx*10+9):
		t = []
		for j in range(9):
			t.append(int(str(data[i])[j]))
		sudoku.append(t)
	total += return3(sudoku)
print("total = ", total)
















