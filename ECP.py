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

sudokuBoard1_2_0 = [[1, 0],
				  [0, 0]]

sudokuBoard1_3_0 = [[1, 0, 0],
				  	[0, 1, 0],
				  	[0, 0, 1]]

sudokuBoard2_2_0 = [[0, 4,  2, 3],
				[3, 2,  4, 1],

				[4, 1,  3, 2],
				[2, 3,  1, 4]]

sudokuBoard2_2_1 = [[1, 0,  0, 0],
				[0, 2,  0, 0],

				[0, 0,  3, 0],
				[1, 0,  0, 4]]

sudokuBoard2_2_2 = [[1, 0,  0, 0],
				[0, 2,  0, 0],

				[0, 0,  3, 0],
				[0, 0,  0, 4]]

sudokuBoard3_3_0 = [[0, 7, 0,  5, 8, 3,  0, 2, 0],
				[0, 5, 9,  2, 0, 0,  3, 0, 0],
				[3, 4, 0,  0, 0, 6,  5, 0, 7],
				
				[7, 9, 5,  0, 0, 0,  6, 3, 2],
				[0, 0, 3,  6, 9, 7,  1, 0, 0],
				[6, 8, 0,  0, 0, 2,  7, 0, 0],
				
				[9, 1, 4,  8, 3, 5,  0, 7, 6],
				[0, 3, 0,  7, 0, 1,  4, 9, 5],
				[5, 6, 7,  4, 2, 9,  0, 1, 3]]

sudokuBoard3_3_1 = [[0, 7, 0,  5, 8, 3,  0, 2, 0],
				[0, 5, 9,  2, 0, 0,  3, 0, 0],
				[3, 4, 0,  0, 0, 6,  5, 0, 7],
				
				[0, 0, 0,  0, 0, 0,  0, 0, 0],
				[0, 0, 0,  6, 9, 7,  0, 0, 0],
				[0, 0, 0,  0, 0, 2,  0, 0, 0],
				
				[0, 0, 0,  0, 0, 0,  0, 0, 0],
				[0, 0, 0,  0, 0, 0,  0, 0, 0],
				[0, 0, 0,  0, 0, 0,  0, 0, 0]]

sudokuBoard4_4_0 = [
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

sudokuBoard4_4_1 = [
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

sudokuBoard5_5_0 = [
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

sudokuBoard6_6_0 = [
	[0, 18, 14, 32, 0, 15, 23, 0, 22, 33, 0, 0, 5, 12, 17, 1, 29, 2, 0, 11, 6, 4, 24, 13, 3, 34, 0, 36, 21, 19, 28, 26, 0, 35, 20, 25],
	[20, 0, 28, 25, 26, 0, 1, 12, 17, 2, 5, 29, 11, 24, 4, 6, 13, 8, 33, 0, 0, 22, 30, 31, 18, 0, 0, 0, 14, 10, 21, 19, 9, 3, 0, 34],
	[0, 29, 17, 12, 1, 2, 0, 34, 21, 9, 36, 0, 27, 32, 14, 10, 0, 15, 16, 0, 26, 28, 25, 35, 31, 30, 33, 7, 22, 23, 4, 6, 8, 13, 11, 24],
	[36, 3, 21, 34, 19, 9, 6, 24, 4, 8, 11, 13, 7, 30, 22, 0, 31, 33, 2, 5, 1, 17, 12, 29, 35, 25, 16, 20, 0, 26, 14, 10, 15, 18, 0, 32],
	[11, 13, 4, 0, 6, 8, 10, 32, 14, 15, 27, 0, 20, 25, 28, 26, 35, 16, 0, 36, 19, 21, 34, 3, 29, 0, 2, 5, 17, 0, 22, 0, 33, 31, 7, 30],
	[7, 31, 22, 30, 23, 33, 26, 0, 28, 16, 20, 35, 36, 34, 0, 19, 3, 9, 15, 27, 10, 14, 32, 18, 13, 24, 8, 11, 4, 6, 17, 0, 2, 29, 0, 12],
	[29, 2, 25, 1, 17, 20, 21, 19, 12, 5, 3, 9, 18, 10, 24, 0, 15, 11, 7, 35, 28, 30, 26, 16, 33, 23, 27, 31, 32, 22, 34, 4, 36, 8, 13, 6],
	[3, 9, 12, 19, 21, 5, 0, 6, 34, 36, 13, 8, 31, 0, 32, 22, 33, 27, 20, 29, 0, 25, 1, 2, 16, 26, 7, 35, 30, 28, 24, 14, 11, 15, 0, 0],
	[13, 8, 34, 6, 4, 0, 14, 0, 24, 11, 18, 0, 35, 26, 0, 28, 16, 7, 5, 3, 21, 12, 19, 0, 2, 0, 20, 29, 0, 17, 32, 22, 27, 33, 0, 23],
	[35, 16, 30, 26, 0, 7, 17, 1, 25, 20, 29, 2, 13, 6, 34, 4, 8, 36, 27, 31, 22, 32, 23, 33, 15, 10, 11, 18, 0, 14, 12, 21, 5, 9, 3, 19],
	[18, 15, 24, 10, 14, 11, 22, 23, 32, 27, 0, 33, 29, 1, 25, 17, 0, 20, 36, 13, 4, 34, 6, 8, 9, 19, 5, 0, 12, 21, 30, 28, 7, 16, 35, 26],
	[31, 0, 0, 23, 22, 27, 28, 26, 30, 7, 35, 16, 3, 19, 12, 21, 9, 5, 11, 18, 14, 24, 0, 15, 8, 6, 36, 13, 34, 4, 25, 17, 20, 0, 0, 1],
	[14, 24, 0, 11, 13, 6, 0, 27, 15, 10, 22, 0, 17, 20, 16, 35, 25, 26, 19, 4, 3, 9, 36, 34, 12, 5, 1, 21, 2, 29, 33, 0, 23, 30, 28, 7],
	[4, 34, 9, 36, 3, 19, 13, 11, 8, 6, 14, 24, 28, 7, 33, 31, 0, 23, 1, 21, 29, 2, 5, 12, 25, 20, 0, 0, 16, 35, 15, 18, 10, 32, 22, 27],
	[0, 30, 33, 7, 31, 23, 35, 20, 16, 26, 17, 25, 4, 36, 9, 3, 34, 19, 10, 22, 18, 15, 27, 32, 24, 0, 6, 0, 0, 13, 2, 0, 1, 12, 21, 5],
	[21, 12, 2, 5, 0, 1, 3, 36, 9, 19, 4, 34, 0, 0, 0, 18, 32, 0, 26, 17, 35, 16, 20, 25, 30, 0, 23, 28, 0, 31, 8, 13, 0, 24, 14, 0],
	[22, 32, 15, 27, 18, 10, 31, 0, 33, 23, 28, 30, 21, 5, 2, 29, 12, 1, 0, 14, 13, 8, 11, 24, 34, 36, 19, 0, 9, 3, 16, 35, 0, 25, 17, 20],
	[17, 25, 16, 0, 35, 26, 29, 5, 2, 1, 21, 12, 14, 11, 8, 13, 24, 0, 23, 28, 31, 33, 7, 30, 0, 0, 10, 22, 15, 18, 9, 3, 19, 34, 4, 36],
	[23, 22, 18, 33, 27, 32, 7, 16, 31, 30, 26, 28, 19, 9, 29, 0, 21, 12, 24, 0, 11, 13, 0, 14, 4, 8, 34, 6, 3, 36, 35, 0, 25, 17, 1, 2],
	[10, 14, 13, 15, 11, 24, 27, 33, 18, 32, 23, 22, 1, 2, 35, 20, 17, 25, 34, 6, 36, 3, 8, 0, 21, 9, 12, 19, 29, 0, 31, 7, 30, 28, 0, 16],
	[26, 28, 31, 16, 7, 30, 20, 2, 0, 25, 1, 17, 6, 8, 3, 36, 4, 34, 32, 0, 27, 18, 33, 22, 14, 15, 24, 10, 13, 11, 29, 5, 12, 21, 19, 9],
	[1, 0, 35, 2, 20, 25, 5, 9, 29, 12, 0, 21, 10, 15, 13, 11, 14, 24, 30, 26, 7, 0, 0, 28, 0, 33, 0, 0, 0, 27, 3, 36, 34, 4, 6, 8],
	[19, 21, 29, 9, 5, 12, 36, 8, 3, 34, 6, 4, 23, 33, 18, 27, 22, 32, 25, 1, 0, 35, 2, 17, 28, 16, 30, 26, 31, 7, 0, 11, 24, 14, 10, 15],
	[6, 4, 0, 8, 0, 34, 11, 15, 13, 24, 0, 14, 26, 16, 31, 0, 28, 30, 12, 19, 5, 29, 9, 21, 17, 0, 25, 1, 0, 0, 18, 0, 0, 22, 0, 0],
	[0, 6, 36, 13, 8, 4, 0, 18, 11, 14, 32, 10, 25, 0, 7, 16, 26, 28, 21, 34, 9, 5, 3, 0, 1, 29, 17, 12, 0, 2, 27, 33, 0, 23, 0, 31],
	[12, 0, 0, 29, 2, 17, 9, 3, 5, 21, 34, 19, 32, 18, 11, 0, 10, 14, 28, 25, 0, 7, 0, 26, 23, 31, 22, 30, 27, 33, 36, 8, 4, 6, 0, 13],
	[34, 19, 5, 3, 9, 21, 8, 13, 0, 4, 24, 6, 30, 31, 27, 33, 23, 22, 17, 12, 2, 20, 29, 1, 26, 35, 0, 0, 7, 16, 11, 15, 14, 10, 32, 18],
	[25, 26, 7, 35, 16, 28, 0, 29, 20, 17, 12, 1, 24, 13, 36, 8, 6, 4, 22, 30, 33, 27, 0, 23, 0, 0, 14, 0, 11, 15, 5, 9, 0, 19, 34, 3],
	[30, 23, 27, 31, 33, 22, 16, 35, 7, 28, 25, 26, 34, 3, 0, 9, 19, 21, 14, 32, 15, 11, 18, 10, 6, 13, 4, 24, 36, 8, 20, 2, 17, 1, 12, 29],
	[32, 10, 11, 18, 15, 14, 33, 0, 27, 22, 30, 23, 12, 29, 20, 2, 1, 17, 0, 24, 8, 36, 0, 6, 19, 3, 21, 34, 0, 9, 7, 16, 0, 26, 0, 35],
	[2, 20, 0, 17, 25, 35, 12, 21, 1, 0, 9, 5, 15, 14, 0, 24, 11, 13, 31, 16, 30, 23, 28, 7, 27, 22, 18, 33, 10, 32, 19, 34, 3, 36, 0, 4],
	[16, 7, 23, 0, 30, 0, 0, 17, 26, 35, 2, 20, 8, 4, 19, 34, 36, 3, 18, 33, 32, 10, 0, 0, 11, 14, 0, 15, 6, 24, 1, 12, 0, 5, 9, 21],
	[8, 36, 0, 0, 0, 3, 24, 0, 6, 13, 15, 0, 16, 0, 23, 30, 7, 0, 29, 9, 0, 1, 0, 0, 20, 17, 35, 2, 26, 25, 10, 32, 0, 27, 33, 22],
	[33, 0, 10, 22, 32, 0, 30, 28, 23, 0, 16, 7, 9, 21, 1, 12, 5, 29, 13, 15, 0, 6, 14, 11, 36, 4, 3, 8, 19, 34, 26, 0, 35, 20, 2, 17],
	[0, 11, 6, 14, 24, 13, 32, 22, 10, 18, 33, 27, 2, 0, 26, 25, 20, 35, 3, 8, 34, 19, 4, 36, 5, 21, 29, 9, 1, 12, 23, 30, 31, 7, 0, 28],
	[9, 5, 1, 0, 12, 29, 34, 4, 19, 3, 8, 36, 0, 0, 10, 32, 27, 18, 0, 0, 25, 26, 17, 20, 7, 28, 31, 16, 23, 30, 6, 24, 0, 0, 15, 14],
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

	def blockID(row, col, blockHeight, blockWidth):
		return (row // blockHeight) * (len(sudoku[0]) // blockWidth) + (col // blockWidth)

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
				row[3 * len(sudoku)**2 + blockID(r, c, blockHeight, blockWidth) * len(sudoku) + (n - 1)] = 1  # Block constraint
				nuRow = clueRow(True, row)
				matrix1.append(nuRow)
			else:
				# Empty cells: Add rows for all possible placements
				for n in range(1, len(sudoku) + 1):
					row = [0] * numConstraints
					row[r * len(sudoku) + c] = 1  # Cell constraint
					row[len(sudoku)**2 + r * len(sudoku) + (n - 1)] = 1  # Row constraint
					row[2 * len(sudoku)**2 + c * len(sudoku) + (n - 1)] = 1  # Column constraint
					row[3 * len(sudoku)**2 + blockID(r, c, blockHeight, blockWidth) * len(sudoku) + (n - 1)] = 1  # Block constraint
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
		

sudokuSolver(sudokuBoard1_3_0, 1, 3)