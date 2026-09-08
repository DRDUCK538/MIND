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


# TESTS
assert move((2, 3), "a") == (2, 2)
assert move((2, 2), "a") == (2, 2)
assert move((0, 2), "w") == (0, 2)
assert move((2, 3), "x") == (2, 3)
assert move((0, 1), "a") == target




#current loop
while agent != target:
   render()
   d = input("What direction do you want to take: ")
   if d == "stop":
      break
   if d not in valid_directions:
      print("INVALID INPUT")
      continue
   agent = (move(agent,d))
   
if agent == target: print("well done ")





