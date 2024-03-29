def pop_bubbles(bubbles, row, col):
  color = bubbles[row][col]
  if color == 0:  # If the cell is empty, do nothing
      return

  rows, cols = len(bubbles), len(bubbles[0])
  stack = [(row, col)]
  visited = set()

  while stack:
      r, c = stack.pop()
      if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or bubbles[r][c] != color:
          continue
      visited.add((r, c))
      stack.append((r + 1, c))
      stack.append((r - 1, c))
      stack.append((r, c + 1))
      stack.append((r, c - 1))

  for r, c in visited:
      bubbles[r][c] = 0

def drop_bubbles(bubbles):
  rows, cols = len(bubbles), len(bubbles[0])
  for col in range(cols):
      empty_cells = [row[col] for row in bubbles].count(0)
      for row in range(rows - 1, -1, -1):
          if bubbles[row][col] == 0:
              empty_cells += 1
          else:
              new_row = row + empty_cells
              if new_row < rows:
                  bubbles[new_row][col] = bubbles[row][col]
              bubbles[row][col] = 0

def solution(bubbles, operations):
  for row, col in operations:
      pop_bubbles(bubbles, row, col)
      drop_bubbles(bubbles)
  return bubbles

# Example
bubbles = [
  [3, 2, 4, 4],
  [3, 1, 2, 1],
  [1, 1, 1, 4],
  [3, 1, 2, 2],
  [3, 3, 3, 4]
]

operations = [[2, 1], [4, 0], [3, 2], [2, 1]]

result = solution(bubbles, operations)
for row in result:
  print(row)
