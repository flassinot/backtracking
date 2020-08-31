import sys

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

def check_empty(board):
  """ board : [[]] """
  for row in board:
    for cell in row:
      if cell == None:
        return False
  return True

def is_valid(board):
  """ checks if board is valid """

  # Check rows
  for row in board:
    if len(set(row)) < 3 or None in set(row):
      return False

  # Check columns
  for c in range(len(board[0])):
    col = []
    for r in range(len(board)):
      col.append(board[r][c])
    # print(col)
    if len(set(col)) < 3 or None in set(col):
      return False

  return True

def copy_board(board):
  copy = []
  for row in board:
    copy.append(row.copy())
  return copy

def solve(board):
  """ Solve the board """
  if check_empty(board):
    print('Solved !')
    print_board(board)
    return True
  else:
    print('continue')
    for r in range(len(board)):
      for c in range(len(board[0])):
        if board[r][c] == None:
          # Replace cell in the board
          for n in [1, 2, 3]:
            board_copy = copy_board(board)
            board_copy[r][c] = n
            print_board(board_copy)
            print()
            if solve(board_copy) and is_valid(board_copy):
              print_board(board_copy)
              return True
            else:
              #backtrack
              board_copy[r][c] = None
        return False              


b = [[None, 2, None], [3, 1, None], [None, 3, None]]
b2 = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
# print_board(b)
# print(check(b2))
print(solve(b))
# print(is_valid(b))
# print(is_valid(b2))
