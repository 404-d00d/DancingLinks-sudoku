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



def exactCoverBinaryMatrix(sudoku, block_height, block_width):
    N = len(sudoku)
    num_constraints = 4 * N**2
    matrix = []
    matrix1 = []

    def blockID(row, col):
        return (row // block_height) * block_width + (col // block_width)

    for r in range(N):
        for c in range(N):
            num = sudoku[r][c]
            if num != 0:
                # Pre-filled cells: Add only the specific placement
                n = num
                row = [0] * num_constraints
                row[r * N + c] = 1  # Cell constraint
                row[N**2 + r * N + (n - 1)] = 1  # Row constraint
                row[2 * N**2 + c * N + (n - 1)] = 1  # Column constraint
                row[3 * N**2 + blockID(r, c) * N + (n - 1)] = 1  # Block constraint
                matrix.append(row)
                nuRow = clueRow(True, row)
                matrix1.append(nuRow)
            else:
                # Empty cells: Add rows for all possible placements
                for n in range(1, N + 1):
                    row = [0] * num_constraints
                    row[r * N + c] = 1  # Cell constraint
                    row[N**2 + r * N + (n - 1)] = 1  # Row constraint
                    row[2 * N**2 + c * N + (n - 1)] = 1  # Column constraint
                    row[3 * N**2 + blockID(r, c) * N + (n - 1)] = 1  # Block constraint
                    matrix.append(row)
                    nuRow = clueRow(False, row)
                    matrix1.append(nuRow)

    return matrix1

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
	def __init__(self, matrix):
		self.header = Node()
		self.columns = []
		
		for colIndex in range(len(matrix[0].getArrayy())):
			colNode = Node(column=colIndex)
			self.columns.append(colNode)

			colNode.left = self.header.left
			colNode.right = self.header
			self.header.left.right = colNode
			self.header.left = colNode
		
		for rowIndex, row in enumerate(matrix):
			lastNode = None
			for colIndex, cell in enumerate(row.getArrayy()):
				if cell == 1:
					newNode = Node(row=rowIndex, column=colIndex)
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
			print("Solution:", solution)
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
			
			# Backtrack
			solution.pop()
			node = row.left
			while node != row:
				self.uncover(self.columns[node.column])
				node = node.left
			
			row = row.down
		
		self.uncover(column)
		return None


sudokuToELC = exactCoverBinaryMatrix(sudokuBoard0, 2, 2)
for c in sudokuToELC:
	if not c.getConstant():
		print(c.getArrayy())
#print(len(sudokuToELC))
dlx = DancingLinks(sudokuToELC)
symbols = dlx.solve()
print(symbols)