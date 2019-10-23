import sys

first = 0
dot = 0
second = 0
board = [[] for i in range(3)]

def selectMove (character):
   global first
   global dot
   global second
   if (character == 'X'):
      first += 1
   elif (character == '0'):
      second +=1
   else:
      dot += 1

def fullRow (character):
   winRows = False
   for row in range(3):
      if (all(position == character for position in board[row])):
         winRows = True
   return winRows

def fullColumn (character):
   winColumn = False
   for row in range(3):
      if (all(board[column][row] == character for column in range(3))):
         winColumn = True
   return winColumn

def fullDiagonal (character):
   winDiag = False
   if (all(board[ind][ind] == character for ind in range(3))):
      winDiag = True
   if (all(board[2-ind][ind] == character for ind in range(3))):
      winDiag = True
   return winDiag

def checkWinner(character):
   return fullRow(character) or fullColumn(character) or fullDiagonal(character)

def filledBoard():
   filled = True
   for row in range(3):
      if (any(board[row][column] == '.' for column in range(3))):
         winDiag = False
   return filled

for row in range(3):
   rowMoves = input()
   for character in rowMoves:
      selectMove(character)
      board[row].append(character)

message = 'illegal'
filled = filledBoard()
firstWin = checkWinner('X')
secondWin = checkWinner('0')
firstTurn = first == second
secondTurn = first == second + 1

if(filled):
   if (secondTurn):
      if (firstWin and not secondWin):
         message = 'the first player won'
      if (not firstWin and not secondWin):
         message = 'draw'
else:
   if (firstTurn):
      if (not firstWin and not secondWin):
         message = 'first'
      if (secondWin and not firstWin):
         message = 'the second player won'
   if (secondTurn):
      if (not firstWin and not secondWin):
         message = 'second'
      if (firstWin and not secondWin):
         message = 'the first player won'
print(message)

