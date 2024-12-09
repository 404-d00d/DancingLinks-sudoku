color_white = "\u001b[37m"
color_cyan = "\u001b[36m"

ecp = [[0, 1, 1],
	   [1, 0, 1],
	   [1, 1, 0],
	   [1, 0, 0]]

#FIND WAY TO CONVERT ROWS IN MATRIX INTO PLACES FOR SUDOKU

ecp1 = [[0, 1, 1, 0],
		[1, 0, 1, 0],
		[1, 1, 0, 0],
		[1, 0, 0, 0],
		[1, 1, 0, 1],
		[0, 0, 0, 1]]

sudokuBoard2 = [[0, 4,  2, 3],
				[3, 2,  4, 1],

				[4, 1,  3, 2],
				[2, 3,  1, 4]]

sudokuBoard2_2 = [[1, 0,  0, 0],
				[0, 2,  0, 0],

				[0, 0,  3, 0],
				[0, 0,  0, 4]]

sudokuBoard3 = [[0, 7, 0,  5, 8, 3,  0, 2, 0],
				[0, 5, 9,  2, 0, 0,  3, 0, 0],
				[3, 4, 0,  0, 0, 6,  5, 0, 7],
				
				[7, 9, 5,  0, 0, 0,  6, 3, 2],
				[0, 0, 3,  6, 9, 7,  1, 0, 0],
				[6, 8, 0,  0, 0, 2,  7, 0, 0],
				
				[9, 1, 4,  8, 3, 5,  0, 7, 6],
				[0, 3, 0,  7, 0, 1,  4, 9, 5],
				[5, 6, 7,  4, 2, 9,  0, 1, 3]]

sudokuBoard3_2 = [[0, 7, 0,  5, 8, 3,  0, 2, 0],
				[0, 5, 9,  2, 0, 0,  3, 0, 0],
				[3, 4, 0,  0, 0, 6,  5, 0, 7],
				
				[0, 0, 0,  0, 0, 0,  0, 0, 0],
				[0, 0, 0,  6, 9, 7,  0, 0, 0],
				[0, 0, 0,  0, 0, 2,  0, 0, 0],
				
				[0, 0, 0,  0, 0, 0,  0, 0, 0],
				[0, 0, 0,  0, 0, 0,  0, 0, 0],
				[0, 0, 0,  0, 0, 0,  0, 0, 0]]

sudokuBoard4 = [
    [1, 12, 2, 3, 8, 4, 16, 13, 10, 14, 0, 7, 11, 5, 15, 6],
    [7, 14, 10, 9, 11, 5, 6, 0, 2, 0, 3, 1, 8, 4, 13, 16],
    [16, 8, 13, 4, 0, 9, 0, 10, 15, 11, 5, 0, 12, 3, 2, 1],
    [6, 11, 15, 5, 12, 3, 1, 0, 0, 8, 4, 0, 14, 9, 10, 7],
    [0, 0, 6, 10, 3, 15, 12, 1, 0, 4, 2, 8, 9, 13, 7, 14],
    [12, 0, 1, 15, 0, 2, 8, 16, 7, 9, 13, 14, 0, 10, 6, 11],
    [8, 0, 16, 0, 9, 13, 14, 7, 6, 0, 10, 11, 3, 15, 1, 12],
    [14, 9, 0, 13, 0, 10, 11, 6, 1, 3, 15, 12, 4, 2, 16, 8],
    [9, 13, 14, 16, 10, 7, 5, 11, 12, 0, 6, 3, 2, 1, 8, 4],
    [5, 10, 11, 7, 15, 6, 3, 12, 8, 2, 1, 4, 13, 16, 14, 0],
    [4, 2, 8, 1, 13, 16, 9, 0, 11, 10, 0, 5, 15, 6, 0, 3],
    [3, 15, 12, 6, 2, 1, 4, 8, 0, 0, 16, 0, 10, 0, 11, 5],
    [10, 7, 5, 14, 0, 11, 15, 3, 4, 1, 12, 2, 16, 8, 0, 13],
    [2, 1, 4, 12, 16, 8, 13, 9, 5, 7, 14, 10, 6, 0, 3, 15],
    [15, 6, 3, 11, 1, 12, 2, 4, 9, 16, 8, 0, 7, 0, 5, 10],
    [13, 16, 9, 8, 7, 14, 10, 5, 0, 6, 11, 0, 1, 12, 0, 2]
]

sudokuBoard4_2 = [
    [1, 12, 2, 3, 8, 4, 16, 13, 0, 14, 0, 7, 11, 5, 15, 6],
    [7, 14, 0, 9, 11, 5, 6, 0, 2, 0, 3, 1, 8, 4, 13, 16],
    [16, 8, 13, 4, 0, 9, 0, 0, 15, 11, 5, 0, 12, 3, 2, 1],
    [6, 11, 15, 5, 12, 3, 1, 0, 0, 8, 4, 0, 14, 9, 0, 7],
    [0, 0, 6, 0, 3, 15, 12, 1, 0, 4, 2, 8, 9, 13, 7, 14],
    [12, 0, 1, 15, 0, 2, 8, 16, 7, 9, 13, 14, 0, 10, 6, 11],
    [8, 0, 16, 0, 9, 13, 14, 7, 6, 0, 10, 11, 3, 15, 1, 12],
    [14, 9, 0, 13, 0, 0, 11, 6, 1, 3, 15, 12, 4, 2, 16, 8],
    [9, 13, 14, 16, 0, 7, 5, 11, 12, 0, 6, 3, 2, 1, 8, 4],
    [5, 10, 11, 7, 15, 6, 3, 12, 8, 2, 1, 4, 13, 16, 14, 0],
    [4, 2, 8, 1, 13, 16, 9, 0, 11, 0, 0, 5, 15, 6, 0, 3],
    [3, 15, 12, 6, 2, 1, 4, 8, 0, 0, 16, 0, 0, 0, 11, 5],
    [0, 7, 5, 14, 0, 11, 15, 3, 4, 1, 12, 2, 16, 8, 0, 13],
    [2, 1, 4, 12, 16, 8, 13, 9, 5, 7, 14, 0, 6, 0, 3, 15],
    [15, 6, 3, 11, 1, 12, 2, 4, 9, 16, 8, 0, 7, 0, 5, 0],
    [13, 16, 9, 8, 7, 14, 0, 5, 0, 6, 11, 0, 1, 12, 0, 2]
]

sudokuBoard5 = [
    [0, 23, 3, 19, 0, 20, 12, 7, 9, 11, 10, 0, 21, 22, 17, 0, 24, 8, 15, 13, 1, 6, 16, 4, 18],
    [22, 25, 21, 17, 10, 0, 15, 13, 24, 0, 12, 20, 11, 7, 9, 18, 1, 6, 4, 0, 19, 23, 14, 2, 3],
    [0, 6, 0, 1, 0, 25, 10, 22, 17, 21, 2, 0, 3, 14, 19, 11, 9, 20, 12, 7, 24, 0, 13, 15, 5],
    [13, 8, 5, 24, 15, 23, 2, 14, 19, 3, 4, 6, 0, 0, 1, 21, 17, 0, 10, 22, 9, 0, 7, 12, 0],
    [0, 20, 11, 9, 12, 6, 4, 16, 1, 18, 15, 8, 5, 13, 24, 3, 19, 23, 2, 14, 17, 25, 0, 10, 21],
    [12, 0, 13, 11, 20, 1, 6, 4, 18, 14, 8, 0, 16, 15, 5, 22, 3, 19, 23, 2, 21, 17, 10, 25, 7],
    [15, 24, 16, 5, 8, 0, 23, 2, 3, 22, 6, 1, 0, 4, 18, 7, 0, 0, 0, 0, 11, 9, 12, 20, 13],
    [4, 1, 14, 0, 6, 17, 25, 10, 0, 7, 23, 19, 22, 0, 3, 13, 11, 9, 20, 12, 0, 0, 15, 0, 16],
    [10, 17, 0, 21, 25, 24, 0, 0, 5, 16, 20, 9, 13, 12, 0, 14, 18, 1, 6, 4, 0, 19, 2, 0, 22],
    [2, 19, 22, 3, 23, 9, 0, 12, 11, 13, 25, 17, 0, 10, 21, 16, 5, 24, 8, 15, 18, 1, 4, 6, 14],
    [5, 4, 1, 6, 16, 10, 22, 3, 25, 17, 14, 2, 19, 18, 23, 9, 20, 12, 0, 21, 8, 15, 0, 0, 24],
    [21, 0, 9, 20, 7, 4, 16, 0, 6, 1, 13, 15, 24, 11, 8, 19, 23, 2, 14, 0, 25, 0, 0, 0, 0],
    [0, 10, 17, 25, 22, 15, 13, 11, 8, 24, 7, 12, 9, 21, 20, 1, 6, 4, 0, 5, 23, 2, 18, 14, 19],
    [11, 15, 24, 8, 13, 2, 0, 18, 23, 19, 16, 4, 1, 5, 6, 17, 0, 0, 22, 3, 20, 12, 21, 7, 9],
    [18, 2, 0, 23, 14, 12, 0, 21, 20, 0, 0, 10, 17, 0, 25, 24, 8, 15, 0, 11, 6, 0, 5, 16, 1],
    [1, 14, 23, 2, 18, 7, 21, 17, 12, 20, 3, 22, 0, 19, 0, 8, 15, 13, 11, 9, 4, 16, 24, 5, 6],
    [9, 13, 8, 15, 11, 14, 18, 0, 2, 0, 5, 16, 6, 24, 4, 25, 10, 22, 3, 19, 12, 7, 17, 21, 20],
    [19, 22, 25, 10, 3, 13, 11, 9, 15, 8, 21, 0, 20, 17, 0, 6, 4, 16, 5, 24, 2, 14, 1, 18, 23],
    [17, 7, 20, 12, 21, 16, 0, 24, 4, 0, 11, 13, 8, 9, 15, 23, 2, 14, 18, 1, 10, 22, 19, 3, 25],
    [24, 16, 6, 0, 5, 22, 3, 19, 10, 25, 18, 14, 0, 1, 2, 20, 12, 7, 21, 17, 15, 13, 9, 11, 0],
    [0, 0, 15, 0, 9, 18, 1, 6, 0, 2, 24, 5, 4, 8, 16, 10, 22, 3, 19, 23, 7, 21, 25, 0, 12],
    [25, 0, 12, 7, 17, 5, 24, 8, 16, 0, 9, 11, 15, 20, 13, 2, 14, 18, 1, 6, 22, 3, 23, 19, 10],
    [8, 5, 4, 16, 24, 3, 19, 23, 22, 10, 0, 18, 2, 6, 14, 12, 7, 21, 17, 25, 13, 11, 0, 9, 0],
    [6, 18, 2, 14, 0, 21, 17, 25, 7, 12, 19, 0, 10, 23, 22, 15, 13, 11, 9, 20, 16, 5, 8, 24, 4],
    [23, 3, 10, 22, 19, 11, 0, 20, 13, 15, 17, 21, 0, 25, 7, 4, 16, 5, 24, 8, 0, 18, 6, 1, 0]
]

def printBoard(board, subRow, subCol, specX, specY):
	for y in range(len(board[0])):
		for x in range(len(board[y])):
			# Highlights most recent number placed for easier reading
			if (specX == x and specY == y):
				print(color_cyan+str(board[y][x])+color_white, end="")
			else:
				print(str(board[y][x]), end="")

			if (x+1)%subCol == 0 and x != len(board[y])-1:
				print("|", end="")
			elif x != len(board[y])-1:
				print(" ", end="")

		if (y+1)%subRow == 0 and y != len(board[x])-1:
			print()
			for z in range(2*len(board[0])-1):
				if (z+1)%(2*subRow) == 0 and (z != len(board[0])*subCol-1 or z != 0):
					print("+", end="")
				else:
					print("-", end="")
		print()
	print()


def rowToPosition(solutionRows, allRows, originalBoard, subRow, subCol):
	nuBoard = originalBoard
	lastRow, lastCol = -1, -1

	for key in solutionRows:
		if key in allRows.keys() and not allRows[key].getConstant():
			solRow = allRows[key]
			rowArray = solRow.getArrayy()

			indices = [i for i, v in enumerate(rowArray) if v == 1]
			cellIndex = indices[0]  # Cell constraint
			rowIndex = indices[1] - len(originalBoard)**2  # Row constraint

			# Map to board position
			row = cellIndex // len(originalBoard)
			col = cellIndex % len(originalBoard)
			num = (rowIndex % len(originalBoard)) + 1

			nuBoard[row][col] = num
			lastRow, lastCol = row, col

			print(str(num)+" in ("+str(col)+", "+str(row)+")")
			print()
			printBoard(nuBoard, subRow, subCol, lastCol, lastRow)
	
	return nuBoard

def exactCoverBinaryMatrix(sudoku, blockHeight, blockWidth):
	numConstraints = 4 * len(sudoku)**2
	matrixDict = {}
	matrix1 = []

	def blockID(row, col):
		return (row // blockHeight) * blockWidth + (col // blockWidth)

	for r in range(len(sudoku)):
		for c in range(len(sudoku)):
			num = sudoku[r][c]
			if num != 0:
				# Pre-filled cells: Add only the specific placement
				n = num
				row = [0] * numConstraints
				row[r * len(sudoku) + c] = 1  # Cell constraint
				row[len(sudoku)**2 + r * len(sudoku) + (n - 1)] = 1  # Row constraint
				row[2 * len(sudoku)**2 + c * len(sudoku) + (n - 1)] = 1  # Column constraint
				row[3 * len(sudoku)**2 + blockID(r, c) * len(sudoku) + (n - 1)] = 1  # Block constraint
				nuRow = clueRow(True, row)
				matrix1.append(nuRow)
			else:
				# Empty cells: Add rows for all possible placements
				for n in range(1, len(sudoku) + 1):
					row = [0] * numConstraints
					row[r * len(sudoku) + c] = 1  # Cell constraint
					row[len(sudoku)**2 + r * len(sudoku) + (n - 1)] = 1  # Row constraint
					row[2 * len(sudoku)**2 + c * len(sudoku) + (n - 1)] = 1  # Column constraint
					row[3 * len(sudoku)**2 + blockID(r, c) * len(sudoku) + (n - 1)] = 1  # Block constraint
					nuRow = clueRow(False, row)
					matrix1.append(nuRow)

	for a in range(len(matrix1)):
		matrixDict[a] = matrix1[a]

	return matrixDict

class clueRow:
	def __init__(self, isConstant, arrayy):
		self.isConstant = isConstant
		self.arrayy = arrayy

	def getArrayy(self):
		return self.arrayy

	def getConstant(self):
		return self.isConstant

class Node:
	def __init__(self, row=None, column=None):
		self.left = self
		self.right = self
		self.up = self
		self.down = self
		self.column = column
		self.row = row

class DancingLinks:
	def __init__(self, matrixDict):
		self.header = Node()
		self.columns = []
		
		# Get the size of the binary array from the first clueRow
		firstClueRow = next(iter(matrixDict.values()))
		constraintNum = len(firstClueRow.getArrayy())
		
		for colIndex in range(constraintNum):
			colNode = Node(column=colIndex)
			self.columns.append(colNode)

			colNode.left = self.header.left
			colNode.right = self.header
			self.header.left.right = colNode
			self.header.left = colNode

		for rowKey, clueRow in matrixDict.items():
			rowArray = clueRow.getArrayy()
			lastNode = None
			for colIndex, cell in enumerate(rowArray):
				if cell == 1:
					newNode = Node(row=rowKey, column=colIndex)
					colHeader = self.columns[colIndex]

					newNode.up = colHeader.up
					newNode.down = colHeader
					colHeader.up.down = newNode
					colHeader.up = newNode

					if lastNode:
						newNode.left = lastNode
						newNode.right = lastNode.right
						lastNode.right.left = newNode
						lastNode.right = newNode
					else:
						lastNode = newNode

	def cover(self, column):
		column.left.right = column.right
		column.right.left = column.left
		row = column.down
		while row != column:
			node = row.right
			while node != row:
				node.down.up = node.up
				node.up.down = node.down
				node = node.right
			row = row.down

	def uncover(self, column):
		row = column.up
		while row != column:
			node = row.left
			while node != row:
				node.down.up = node
				node.up.down = node
				node = node.left
			row = row.up
		column.left.right = column
		column.right.left = column

	def selectColumn(self):
	    column = None
	    minSize = float('inf')
	    node = self.header.right
	    while node != self.header:
	        size = 0
	        temp = node.down
	        while temp != node:
	            size += 1
	            temp = temp.down
	        if size < minSize:
	            minSize = size
	            column = node
	        node = node.right
	    return column


	def solve(self, solution=[]):
		if self.header.right == self.header:
			#print("Solution:", solution)
			return solution
		
		column = self.selectColumn()
		self.cover(column)
		
		row = column.down
		while row != column:
			solution.append(row.row)
			
			node = row.right
			while node != row:
				self.cover(self.columns[node.column])
				node = node.right
			
			if self.solve(solution):
				return solution
			
			solution.pop()
			node = row.left
			while node != row:
				self.uncover(self.columns[node.column])
				node = node.left
			
			row = row.down
		
		self.uncover(column)
		return None

def sudokuSolver(board, subColSize, subRowSize):
	print("INITIAL BOARD:")
	printBoard(board, subColSize, subRowSize, -1, -1)
	print()
	sudokuToELC = exactCoverBinaryMatrix(board, subColSize, subRowSize)
	# for values in sudokuToELC.values():
	# 	print("IS THIS ARRAY A CONSTANT?",values.getConstant())
	# 	print(values.getArrayy())
	dlx = DancingLinks(sudokuToELC)
	solutionSymbols = dlx.solve()
	if solutionSymbols != None:
		solvedBoard = rowToPosition(solutionSymbols, sudokuToELC, board, subColSize, subRowSize)
	else:
		print("NO SOLUTION TO THE BOARD!")
		

sudokuSolver(sudokuBoard2_2, 2, 2)