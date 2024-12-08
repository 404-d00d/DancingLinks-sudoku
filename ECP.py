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

sudokuBoard0 = [[0, 4,  2, 3],
				[3, 2,  4, 1],

				[4, 1,  3, 2],
				[2, 3,  1, 4]]

sudokuBoard1 = [[0, 7, 0,  5, 8, 3,  0, 2, 0],
				[0, 5, 9,  2, 0, 0,  3, 0, 0],
				[3, 4, 0,  0, 0, 6,  5, 0, 7],
				
				[7, 9, 5,  0, 0, 0,  6, 3, 2],
				[0, 0, 3,  6, 9, 7,  1, 0, 0],
				[6, 8, 0,  0, 0, 2,  7, 0, 0],
				
				[9, 1, 4,  8, 3, 5,  0, 7, 6],
				[0, 3, 0,  7, 0, 1,  4, 9, 5],
				[5, 6, 7,  4, 2, 9,  0, 1, 3]]

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
		N = len(firstClueRow.getArrayy())  # Number of constraints
		
		for colIndex in range(N):
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
		return self.header.right

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
	dlx = DancingLinks(sudokuToELC)
	solutionSymbols = dlx.solve()
	solvedBoard = rowToPosition(solutionSymbols, sudokuToELC, board, subColSize, subRowSize)

#sudokuSolver(sudokuBoard0, 2, 2)
sudokuSolver(sudokuBoard1, 3, 3)