#currently check if for n by n sudoku boards
import math

sudokuBoard1 = [[0, 7, 0,  5, 8, 3,  0, 2, 0],
				[0, 5, 9,  2, 0, 0,  3, 0, 0],
				[3, 4, 0,  0, 0, 6,  5, 0, 7],
				
				[7, 9, 5,  0, 0, 0,  6, 3, 2],
				[0, 0, 3,  6, 9, 7,  1, 0, 0],
				[6, 8, 0,  0, 0, 2,  7, 0, 0],
				
				[9, 1, 4,  8, 3, 5,  0, 7, 6],
				[0, 3, 0,  7, 0, 1,  4, 9, 5],
				[5, 6, 7,  4, 2, 9,  0, 1, 3]]

sudokuBoard2 = [[7, 7, 0,  5, 8, 3,  0, 2, 0],
				[0, 5, 9,  2, 0, 0,  3, 0, 0],
				[3, 4, 0,  0, 0, 6,  5, 0, 7],
				
				[7, 9, 5,  0, 0, 0,  6, 3, 2],
				[0, 0, 3,  6, 9, 7,  1, 0, 0],
				[6, 8, 0,  0, 0, 2,  7, 0, 0],
				
				[9, 1, 4,  8, 3, 5,  0, 7, 6],
				[0, 3, 0,  7, 0, 1,  4, 9, 5],
				[5, 6, 7,  4, 2, 9,  0, 1, 3]]

sudokuBoard3 = [[7, 7, 0,  5, 8, 3,  0, 2, 0],
				[0, 5, 9,  2, 0, 0,  3, 0, 0],
				[3, 4, 0,  0, 0, 6,  5, 0, 7],
				
				[7, 9, 5,  0, 0, 0,  6, 3, 2],
				[0, 0, 3,  6, 9, 7,  1, 0, 0],
				[6, 8, 0,  0, 0, 2,  7, 0, 0],
				
				[9, 1, 4,  8, 3, 5,  0, 7, 6],
				[0, 3, 0,  7, 0, 1,  4, 9, 5],
				[5, 6, 7,  4, 2, 9,  5, 1, 3]]

class Node:
	def __init__(self):
		self.left = self
		self.right = self
		self.top = self
		self.bottom = self
		self.column = None

def noDuplicates(board, rowSize, columnSize):
    duplicatesPresent = False

    for x in range(rowSize):
        seen = set()
        for y in range(columnSize):
            if board[x][y] != 0:
                if board[x][y] in seen:
                    print("There are matching numbers in Row", x)
                    duplicatesPresent = True
                    break
                seen.add(board[x][y])

    for x in range(columnSize):
        seen = set()
        for y in range(rowSize):
            if board[y][x] != 0:
                if board[y][x] in seen:
                    print("There are matching numbers in Column", x)
                    duplicatesPresent = True
                    break
                seen.add(board[y][x])

    gridRowSize = int(math.sqrt(rowSize))
    gridColSize = int(math.sqrt(columnSize))
    for gridRow in range(0, rowSize, gridRowSize):
        for gridCol in range(0, columnSize, gridColSize):
            seen = set()
            for x in range(gridRow, gridRow + gridRowSize):
                for y in range(gridCol, gridCol + gridColSize):
                    if board[x][y] != 0:
                        if board[x][y] in seen:
                            print("There are matching numbers in Grid starting at ("+str(gridRow)+", "+str(gridCol)+")")
                            duplicatesPresent = True
                            break
                        seen.add(board[x][y])

    if not duplicatesPresent:
        print("No duplicates")
    return duplicatesPresent

noDuplicates(sudokuBoard1, 9, 9)
print()
noDuplicates(sudokuBoard2, 9, 9)
print()
noDuplicates(sudokuBoard3, 9, 9)
print()