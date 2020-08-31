# Backtrack(x)
#     if x is not a solution
#         return false
#     if x is a new solution
#         add to list of solutions
#     backtrack(expand x)

elements = ['b1', 'b2', 'g']

solutions = []

def valid(x):
  if len(x) >= 2 and x[1] == 'g': # constraint : girl not allowed on middle bench
    return False
  return True

def backtrack(x):
  """ Main algorithm """

  if valid(x):

    # If the candidate solution is valid and complete return True
    if len(x) == 3:
      solutions.append(x)
      return True

    # If the candidate is incomplete (not a solution yet)
    else:
      for e in elements:
        if e not in x:
          x_copy = x.copy()
          x_copy.append(e)
          backtrack(x_copy)

  return False


# print(expand([]))
# print(expand(['b1']))
# print(expand(['g', 'b2']))
# print(expand(['g', 'b2', 'b1']))

# print(valid(['g', 'b2', 'b1']))
# print(valid(['b2', 'g', 'b1']))

backtrack([])
print('solutions : ' + str(solutions))
