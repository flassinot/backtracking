import sys

# Backtrack(x)
#     if x is not a solution
#         return false
#     if x is a new solution
#         add to list of solutions
#     backtrack(expand x)

elements = [1, 2, 3]

solutions = []

def print_board(board):
  """ Print the board """
  for row in board:

    sys.stdout.write('|')
    
    for cell in row:
      if cell == None:
        sys.stdout.write('_')
      else:
        sys.stdout.write(str(cell))
      sys.stdout.write('|')

    print('')

def valid(board):
  ''' Checks if board is valid (no same values) '''

  # Check lines
  for l in board:
    for e in elements:
      if l.count(e) > 1:
        return False

  # Check columns
  for col in range(len(board[0])):
    column_elements = []
    for row in range(len(board)):
      column_elements.append(board[row][col])

    for e in elements:
      if column_elements.count(e) > 1:
        return False

  return True

def is_complete(board):
  ''' Checks if board is complete (no None)'''
  for row in board:
    if None in row:
      return False
  return True

def next_empty(board):
  ''' Returns next empty slot on board (None)'''

  for irow in range(len(board)):
    for icol in range(len(board[0])):
      if board[irow][icol] == None:
        return (irow, icol)

  return ()

def deep_copy(board):
  copy = []
  for row in board:
    copy.append(row.copy())
  return copy

def create_empty():

  result = []
  for irow in range(3):
    row = []
    for icol in range(3):
      row.append(None)
    result.append(row)

  return result

def backtrack(x):
  """ Main algorithm """

  if valid(x):

    # If the candidate solution is valid and complete return True
    if is_complete(x):
      solutions.append(x)
      return True

    # If the candidate is incomplete (not a solution yet)
    else:
      # Try to put an element on the board if not already present
      # Find next empty slot
      (irow, icol) = next_empty(x)

      for e in elements:
        x_copy = deep_copy(x)
        x_copy[irow][icol] = e
        backtrack(x_copy)

  return False

b = [[None, 2, None], [3, None, None], [None, 3, None]]
b1 = [[2, 2, None], [3, 1, None], [None, 3, None]]
b2 = [
  [1, 2, 3], 
  [3, 1, 2], 
  [2, 3, 1]]

print_board(b)
print()
backtrack(b)

for sol in solutions:
  print_board(sol)
  print()
