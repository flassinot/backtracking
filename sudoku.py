import sys

# Backtrack(x)
#     if x is not a solution
#         return false
#     if x is a new solution
#         add to list of solutions
#     backtrack(expand x)

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]

solutions = []

def print_board(board):
  """ Print the board """

  print()
  for row in board:

    sys.stdout.write('|')
    
    for cell in row:
      if cell == None:
        sys.stdout.write('_')
      else:
        sys.stdout.write(str(cell))
      sys.stdout.write('|')

    print('')
  print()

def is_block_valid(board, i = 0, j = 0):
  """ Check a block. i and j represent starting row and column """

  l = []

  for row in range(i * 3, i * 3 + 3):
    for col in range(j * 3, j * 3 + 3):
      l.append(board[row][col])
  
  for e in elements:
    if l.count(e) > 1: # check if all elements are present exactly once
      return False

  return True

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

  # Check blocks
  for block_row in range(3):
    for block_col in range(3):

      if not is_block_valid(board, block_row, block_col):
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


def backtrack(x):
  """ Main algorithm """

  if valid(x):

    # If the candidate solution is valid and complete return True
    if is_complete(x):
      solutions.append(x)
      print()
      print('Found a solution !')
      print_board(x)
      return True

    # If the candidate is incomplete (not a solution yet)
    elif len(solutions) <= 5:
      # Try to put an element on the board if not already present
      # Find next empty slot
      (irow, icol) = next_empty(x)
      print(f'\r{irow}, {icol} solutions:{len(solutions)}', end='')

      for e in elements:
        x_copy = deep_copy(x)
        x_copy[irow][icol] = e
        backtrack(x_copy)

  return False

# b = [
#   [None, None, None, 4,5,2, None, None, None], 
#   [None, 2, None, None, 7, None, None, 4, None],
#   [None, 4, None, None, None, None, None, 8, None],
#   [1, None, 4, None, None, None, 8, None, 7],
#   [None, None, None, 9, None, 7, None, None, None],
#   [7, 9, None, None, None, None, None, 2, 1],
#   [None, None, 2, None, None, None, 6, None, None],
#   [None, None, None, 2, None, 6, None, None, None, ],
#   [5, None, 7, None, None, None, 2, None, 8]
#   ]

b = [
  [None, None, None, None, None, None, 2, 1, None], 
  [7, None, 1, None, 2, 8, None, 5, 3],
  [None, 3, None, None, 1, 5, None, None, None],
  [9, None, 3, 4, None, None, None, None, 5],
  [5, 2, None, 8, None, None, 1, 4, None],
  [4, None, 7, 1, None, None, None, None, 6],
  [None, 5, None, None, 9, 4, None, None, None],
  [1, None, 4, None, 6, 7, None, 8, 2],
  [None, None, None, None, None, None, 9, 6, None]
  ]

print_board(b)
print()
backtrack(b)
print()
print('---------------------------')
print('Finished backtracking')
print(f'Solutions : {len(solutions)}')
print()
