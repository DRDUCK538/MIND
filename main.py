#grid varibles
rows = 5
cols = 5
agent = (2,3)
target = (0,0)
obstacles = {
   
    (2,1),
    (2,4),
    (1,2),
    (3,2),
    }
valid_directions = {"w", "a", "s", "d"}


#functions
def render():
   for row in range(rows):
      for col in range(cols):
         coords = (row,col)
         if coords == agent:
            print("A", end=" ")
         elif coords == target:
            print("T", end=" ")
         elif coords in obstacles:
            print("#", end=" ")
         elif coords in path:
            print("*", end=" ")
         else:
            print(".", end=" ")
      print("")
def move(pos, d):
    row, col = pos
    if d == "w":
      row -= 1
    elif d == "a":
      col -= 1
    elif d == "s":
      row += 1
    elif d == "d":
      col += 1
    else:
       return pos
    new_pos = (row, col)
    if new_pos not in obstacles and 0 <= row < rows and 0 <= col < cols:
       return new_pos
    else:
       return pos
def neighbours(position):
   row, col = position
   possible_moves= [
      (row - 1, col),
      (row + 1, col),
      (row, col - 1),
      (row, col + 1),]
   legal = []
   for i in possible_moves:
      move_row, move_col = i
      if i not in obstacles and  0 <= move_row < rows and 0 <= move_col < cols:
         legal.append(i)
   return legal
  



# TESTS
assert move((2, 3), "a") == (2, 2)
assert move((2, 2), "a") == (2, 2)
assert move((0, 2), "w") == (0, 2)
assert move((2, 3), "x") == (2, 3)
assert move((0, 1), "a") == target



#BFS
order = []
came_from = {}
start = agent
frontier = [start]
visited = {start}

while frontier:
   current = frontier.pop(0)
   order.append(current)
   if current == target:
      print("found target")
      break
   for next_position in neighbours(current):
      if next_position not in visited:
       came_from[next_position] = current
       visited.add(next_position)
       frontier.append(next_position)

path = [target]
current = target
while current != start:
   current = came_from[current]
   path.append(current)

path.reverse()
#print(path)
#print("visited:", visited)
#print("came_from:", came_from)

render()
   












