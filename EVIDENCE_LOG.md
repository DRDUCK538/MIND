## MIND-0.2 



### Problem
Build a reliable Gridworld with legal movement and basic tests.

### Concepts
Tuples, sets, nested loops, functions, return values, bounds checking, assertions.

### What I built
A 5x5 Gridworld with an agent, target, obstacles, rendering and movement.

### Bug
The agent position changed internally but the displayed grid did not update.

### Cause
I was rendering at the wrong point in the program and also reused row/col variables.

### Fix
Separated movement into a function and rendered the updated agent state correctly.

### Tests
- valid movement
- obstacle collision
- boundary collision
- invalid command
- target movement

### Understanding
I can explain how move(pos, d) changes coordinates and rejects illegal moves.

### Remaining weakness
coding


## MIND-1.1 — BFS Path Reconstruction

### Problem
Make MIND find a route from the agent to the target automatically instead of relying on manual movement.

### Concepts
- Breadth-First Search (BFS)
- FIFO queue
- frontier
- visited set
- neighbours
- parent tracking
- dictionaries
- path reconstruction

### My implementation
I used a frontier starting with the agent position and a visited set to prevent positions being explored more than once.

For each current position, I checked its legal neighbours. Newly discovered positions were added to the frontier and visited set.

I also used a `came_from` dictionary to store which position each new position was reached from.

### Hypothesis
Because BFS explores states in FIFO order, I expected it to find a shortest path through the unweighted grid.

### Experiment
I printed the exploration order, visited states and `came_from` dictionary to check how BFS was exploring the grid.

I then followed the `came_from` links backwards from the target to the start.

### Result
BFS successfully found the target.

The reconstructed path was:

`(2,3) → (1,3) → (0,3) → (0,2) → (0,1) → (0,0)`

I rendered this route on the Gridworld using `*`.

### Bug / Difficulty
At first I confused the full list returned by `neighbours()` with a single neighbour.

I also initially found path reconstruction confusing because `came_from` stores:

`child → parent`

rather than the other way around.

### Cause
I had not fully separated:
- the list of neighbours
- one individual neighbour
- the current state
- the parent of a state

### Fix
I looped through each neighbour individually.

When a new position was discovered, I stored:

`came_from[next_position] = current`

Then I started at the target and repeatedly used:

`current = came_from[current]`

until I reached the start, before reversing the path.

### Understanding
I can now explain:
- why BFS uses FIFO
- what the frontier represents
- why visited states are marked when discovered
- how `came_from` stores parent relationships
- how BFS reconstructs the route after reaching the target

### Remaining weakness
I still need more practice tracing BFS manually and understanding how different frontier behaviour changes BFS into DFS.

### Evidence
- `main.py`
- Git commit: `add BFS path reconstruction`
- Git commit: `render BFS shortest path`
i still need more practice explaining function parameters 

### Evidence
main.py
Git commit: complete MIND-0 gridworld foundations
