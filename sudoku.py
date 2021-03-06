"""
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

Examples
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
"""

def valid(board):
    print(len(board))
    print(len(board[0]))
    for x_index, key  in enumerate(board):
      out = 0
      for y_index, y_key in enumerate(key):
          out +=y_key
      if out != 45:
        print(False)
      
    
def valid_solution(board):
    print(board)
    for k in board:
        out =0 
        for a in k:
            out +=a
        if out != 45:
            return False
    return True


def myValid(board):
  for i in range(len(board)):
    hAdd =0 
    vAdd = 0
    print("i >", board[i])
    for j in range(len(board)):
      hAdd += board[i][j] 
      vAdd += board[j][i] 
      if board[i][j] < 1 and board[i][j] > 9 :
        return False
      if hAdd != 45 or vAdd != 45:
        return False

def validSolution(board):

    for i in range(len(board)):
        hadd = 0
        vadd = 0
        for j in range(len(board)):
            #vertical check
            vadd += board[j][i]
            #horizontal check
            hadd += board[i][j]
            #numbers check
            if board[i][j] < 1 or board[i][j] > 9:
                print(1)
                return False
        if vadd != 45 or hadd != 45:
            print (2)
            print (vadd)
            print (hadd)
            return False
    
    return True 


def validSolution(board):

    for i in range(len(board)):
        hadd = 0
        vadd = 0
        for j in range(len(board)):
            #vertical check
            vadd += board[j][i]
            #horizontal check
            hadd += board[i][j]
            #numbers check
            if board[i][j] < 1 or board[i][j] > 9:
                print(1)
                return False
        if vadd != 45 or hadd != 45:
            print (2)
            print (vadd)
            print (hadd)
            return False
    for i in range(3):
        for j in range(3):
            gadd = 0
            for k in range(3):
                for l in range(3):
                    gadd += board[i*3+k][j*3+l]
                    if board[i][j] < 1 or board[i][j] > 9:
                        print (3)
                        return False
            if gadd != 45:
                return False
    return True 

b = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]
#valid(b)
b = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
myValid(b)