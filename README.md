# Lab-1-Uninformed-Search-Informed-Search


## Inroduction to Artificial Intelligence
* Instructor: Nguyen Bao Long
* Time: 13/03/2023

## Requirements
### 1. Study & Report 
* State components of a search problem. Diﬀerentiate Informed search and Uninformed search.
* State the solution (in pseudo-code) of a search problem.
* Report about 4 searching algorithms DFS, BFS, UCS, A∗. The following contents should be included:
  * General idea of the algorithm.
  * Pseudo-code.
  * Properties of algorithm (completeness, optimal, time complexity, space complexity).
  * Defnition of heuristic in A∗. List some options of heuristic
  
### 2. Comparison  
* Compare between UCS, Greedy and A*
* Compare between UCS, Dijkstra

### 3. Implementation
![image](https://user-images.githubusercontent.com/76527212/226888275-b97e0cc0-8a90-4c18-a22b-2950f7fa235f.png)

* File **./src/Space.py** defnes a state space, contains **class Node** and **class
Graph**.
  * **class Node** defnes a node object and supported functions.
  * **class Graph** defnes a graph object and supported functions.
* File **./src/SearchAlgorithms.py** is where you implement searching algorithms. You can design other supported functions as well as use the
following hints (or not). However, you must not change the parameters of
all given functions. Hints:
  * **open_set**: Contains nodes that are extended to.
  * **closed_set**: Contains nodes that were taken out of open_set.
  * **father**: If node x extends to node y, then **father[y] = x**.
  * **cost**: If cumulative cost from start state to state x is y, then **cost[x]
= y**.
* File **./src/Constants.py:** Contains constants. Do not change the value
any variable in this fle.
* File **./src/main.py:** You can run the program by calling this fle. For
example:
> python main.py --algo AStar --start 71 --goal 318


