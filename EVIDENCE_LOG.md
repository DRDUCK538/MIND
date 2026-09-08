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
i still need more practice explaining function parameters 

### Evidence
main.py
Git commit: complete MIND-0 gridworld foundations