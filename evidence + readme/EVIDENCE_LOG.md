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


## MIND-1.2 — DFS Comparison

### Problem
Compare DFS with BFS and understand how changing the frontier changes search behaviour.

### Concepts
- stack
- LIFO
- DFS
- exploration order
- path length
- nodes explored
- neighbour ordering

### My implementation
I changed the BFS frontier from removing the first item with `pop(0)` to removing the last item with `pop()`.

This changed the search from FIFO to LIFO and therefore from BFS to DFS.

### Experiment
I compared BFS and DFS on the same Gridworld.

I then changed only the order of neighbours returned by `neighbours()` and reran DFS.

### Result
DFS sometimes found a longer path and explored more nodes than BFS.

After changing neighbour order, DFS performed much better.

### Understanding
DFS explores one branch deeply before trying alternatives.

DFS does not guarantee the shortest route and its performance can change significantly depending on neighbour order.

BFS guarantees a shortest path on my unweighted Gridworld.

### Remaining weakness
I should get more practice predicting DFS exploration order manually.


## MIND-1.3 — UCS / Dijkstra

### Problem
Make MIND find the cheapest route when different squares have different movement costs.

### Concepts
- weighted costs
- priority queue
- `heapq`
- `cost_so_far`
- cheapest known route
- path cost
- updating a state when a cheaper route is found

### My implementation
I created a dictionary containing costs for expensive terrain.

Normal tiles default to cost 1.

I used a priority queue so the search explores the state with the lowest total cost so far.

For every neighbour I calculated:

`new_cost = current_cost + get_cost(next_position)`

If the state had never been reached before, or the new route was cheaper, I updated:
- `cost_so_far`
- `came_from`
- the priority queue

### Experiment
I created terrain where the shortest route in number of moves was not the cheapest route.

### Result
Dijkstra deliberately chose a route with more moves when that route had a lower total cost.

On one comparison map:
- Dijkstra path cost = 13
- path length = 5
- nodes explored = 17

### Understanding
BFS minimises number of moves.

Dijkstra minimises total path cost.

Dijkstra needs a priority queue because it must explore the cheapest known state next instead of simply exploring the oldest state.


## MIND-1.4 — A*


### Problem
Improve Dijkstra by using information about how close each state appears to be to the target.

### Concepts
- heuristic
- Manhattan distance
- `g(n)`
- `h(n)`
- `f(n) = g(n) + h(n)`
- admissibility
- optimality

### My implementation
I implemented Manhattan distance:

`abs(row - target_row) + abs(col - target_col)`

For A*:
- `g(n)` = actual path cost so far
- `h(n)` = Manhattan-distance estimate to the target
- priority = `g(n) + h(n)`

A* reused most of my Dijkstra implementation but changed the priority used by the heap.

### Experiment 1 — A* vs Dijkstra
On the same weighted map:

Dijkstra:
- path cost = 13
- path length = 5
- nodes explored = 17

A*:
- path cost = 13
- path length = 5
- nodes explored = 12

### Result
Both found the same cheapest path, but A* explored 5 fewer nodes.

The heuristic helped direct the search toward the goal.

### Experiment 2 — Overestimating heuristic
I changed the map so:
- the cheapest route cost 9
- a shorter-looking route cost 10

Results:

Dijkstra:
- cost = 9

A* with normal Manhattan distance:
- cost = 9

A* with `3 × Manhattan distance`:
- cost = 10

### Result
The overestimating heuristic caused A* to miss the optimal route.

### Understanding
A* still tries to find the cheapest path.

Unlike Dijkstra, it also estimates the remaining distance to the target.

A good heuristic can reduce the number of states explored while preserving optimality.

An overestimating heuristic can cause A* to lose its optimal-path guarantee.

### Remaining weakness
I want to become faster at tracing priority queues and explaining why admissibility guarantees matter.

### Evidence
- `main.py`
- BFS / DFS comparison
- weighted Dijkstra experiment
- A* vs Dijkstra node comparison
- overestimating heuristic experiment
- Git commit: `implement A* and test heuristic admissibility`





##### learning rate matters

 ####