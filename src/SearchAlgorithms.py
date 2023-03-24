from Space import *
from Constants import *
import math as math_
from time import *

def setColorPath(g: Graph, path, sc: pygame.surface):
    g.goal.set_color(purple)
    drawNode(g.goal, sc)
    child = g.goal.value
    while child != g.start.value:
        pygame.draw.line(sc, green, (g.grid_cells[child].x, g.grid_cells[child].y), (
            g.grid_cells[path[child]].x, g.grid_cells[path[child]].y), 2)
        pygame.display.flip()
        child = path[child]
        g.grid_cells[child].set_color(grey)
        g.draw(sc)
    g.start.set_color(orange)
    drawNode(g.start, sc)

def costTwoNode(a: Node, b: Node):
    cost = math_.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    return cost


def getNodeMinCost(open_set: list[Node], g: Graph, cost: list[Node]):
    min = g.get_len() # min = len of graph
    temp = open_set[0] # temp = first node
    for i in open_set:
        if cost[i.value] < min:
            min = cost[i.value]
            temp = i
    return temp

def getHeuristic(g: Graph, a: Node):
    goal = g.goal
    cost = int(math_.sqrt((a.x - goal.x)**2 + (a.y - goal.y)**2))
    return cost

def getNodeMinCostHeuristic(open_set: list[Node], g: Graph, cost: list[Node]):
    min = 10**8
    temp = open_set[0] # temp = first node
    for i in open_set:
        if (cost[i.value] + getHeuristic(g, i)) < min:
            min = cost[i.value] + getHeuristic(g, i)
            temp = i
    return temp


def drawNode(node: Node, sc: pygame.Surface):
    node.draw(sc)
    pygame.display.flip()
    sleep(0.1)

# Implement algorithms
def DFS(g: Graph, sc: pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    # TODO: Implement DFS algorithm using open_set, closed_set, and father

    # draw start node
    g.start.set_color(orange)
    drawNode(g.start, sc)
    while open_set:

        # draw current node
        currentNode = open_set.pop(0)
        currentNode.set_color(yellow)
        drawNode(currentNode, sc)

        # append closed node
        closed_set.append(currentNode)

        currentNode.set_color(blue)
        drawNode(currentNode, sc)

        # Check if current node is goal
        if g.is_goal(currentNode):
            currentNode.set_color(purple)
            setColorPath(g, father, sc)
            return

        # list new neighbors
        newNeighbors = []
        for neighbor in g.get_neighbors(currentNode):
            if neighbor not in closed_set and neighbor not in open_set:
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    drawNode(neighbor, sc)
                father[neighbor.value] = currentNode.value
                newNeighbors.append(neighbor)

        # add list neighbors to open_set
        open_set[:0] = newNeighbors


def BFS(g: Graph, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    # TODO: Implement BFS algorithm using open_set, closed_set, and father

    # draw start node
    g.start.set_color(orange)
    drawNode(g.start, sc)
    while open_set:

        # draw current node
        currentNode = open_set.pop(0)
        currentNode.set_color(yellow)
        drawNode(currentNode, sc)

        # append closed node
        closed_set.append(currentNode)

        currentNode.set_color(blue)
        drawNode(currentNode, sc)

        # Check if current node is goal
        if g.is_goal(currentNode):
            currentNode.set_color(purple)
            setColorPath(g, father, sc)
            return
        # list new neighbors
        newNeighbors = []
        for neighbor in g.get_neighbors(currentNode):
            if neighbor not in closed_set and neighbor not in open_set:
                newNeighbors.append(neighbor)
                father[neighbor.value] = currentNode.value
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    drawNode(neighbor, sc)

        # add list neighbors to open_set
        open_set.extend(newNeighbors)


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    
     # draw start node
    g.start.set_color(orange)
    drawNode(g.start, sc)
    while open_set:

        # draw current node
        currentNode = getNodeMinCost(open_set, g, cost) # current node cost min
        currentNode.set_color(yellow)
        drawNode(currentNode, sc)

        # append closed node
        closed_set.append(currentNode)

        currentNode.set_color(blue)
        drawNode(currentNode, sc)

        open_set.remove(currentNode)

        # Check if current node is goal
        if g.is_goal(currentNode):
            currentNode.set_color(purple)
            setColorPath(g, father, sc)
            return
        # list new neighbors and update cost
        newNeighbors = []
        for neighbor in g.get_neighbors(currentNode):
            if neighbor not in closed_set and neighbor not in open_set:
                newNeighbors.append(neighbor)
                father[neighbor.value] = currentNode.value
                cost[neighbor.value] = costTwoNode(currentNode, neighbor) + cost[currentNode.value]
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    drawNode(neighbor, sc)
        # add list neighbors to open_set
        open_set.extend(newNeighbors)
        
        


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement A* algorithm using open_set, closed_set, and father
    
    # draw start node
    g.start.set_color(orange)
    drawNode(g.start, sc)
    while open_set:

        # draw current node
        currentNode = getNodeMinCostHeuristic(open_set, g, cost) # current node cost min
        currentNode.set_color(yellow)
        drawNode(currentNode, sc)

        # append closed node
        closed_set.append(currentNode)

        currentNode.set_color(blue)
        drawNode(currentNode, sc)

        open_set.remove(currentNode)

        # Check if current node is goal
        if g.is_goal(currentNode):
            currentNode.set_color(purple)
            setColorPath(g, father, sc)
            return
        # list new neighbors and update cost
        newNeighbors = []
        for neighbor in g.get_neighbors(currentNode):
            if neighbor not in closed_set and neighbor not in open_set:
                newNeighbors.append(neighbor)
                father[neighbor.value] = currentNode.value
                
                #update cost
                cost[neighbor.value] = cost[currentNode.value] + costTwoNode(currentNode, neighbor) 

                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    drawNode(neighbor, sc)

        # add list neighbors to open_set
        open_set = (newNeighbors)

def IDDFS(g: Graph, sc: pygame.Surface):
    print('Implement IDDFS algorithm')


    father = [-1]*g.get_len()
    depth = 0
    # TODO: Implement DFS algorithm using open_set, closed_set, and father

    # draw start node
    g.start.set_color(orange)
    drawNode(g.start, sc)
    while True:
        open_set = [(g.start, 0)]
        closed_set = []
        while open_set:

            # draw current node
            (currentNode, currentDepth) = open_set.pop(0)
            currentNode.set_color(yellow)
            drawNode(currentNode, sc)

            # append closed node
            closed_set.append(currentNode)

            currentNode.set_color(blue)
            drawNode(currentNode, sc)

            # Check if current node is goal
            if g.is_goal(currentNode):
                currentNode.set_color(purple)
                setColorPath(g, father, sc)
                return

            if currentDepth > depth:
                continue
            # list new neighbors
            newNeighbors = []
            for neighbor in g.get_neighbors(currentNode):
                if neighbor not in closed_set and neighbor not in open_set:
                    if neighbor.value != g.goal.value:
                        neighbor.set_color(red)
                        drawNode(neighbor, sc)
                    father[neighbor.value] = currentNode.value
                    newNeighbors.append((neighbor, currentDepth + 1))

            # add list neighbors to open_set
            open_set[:0] = newNeighbors
        depth += 1
