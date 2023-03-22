from Space import *
from Constants import *


def set_Color_Path(g: Graph, path, sc: pygame.surface):
    g.goal.set_color(purple)
    g.draw(sc)
    child = g.goal.value
    while child != g.start.value:
        pygame.draw.line(sc, green, (g.grid_cells[child].x, g.grid_cells[child].y), (
            g.grid_cells[path[child]].x, g.grid_cells[path[child]].y), 2)
        pygame.display.flip()
        child = path[child]
        g.grid_cells[child].set_color(grey)
        g.draw(sc)
    g.start.set_color(orange)
    g.draw(sc)


def DFS(g: Graph, sc: pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    # TODO: Implement DFS algorithm using open_set, closed_set, and father

    # draw start node
    g.start.set_color(orange)
    g.draw(sc)
    while open_set:

        # draw current node
        currentNode = open_set.pop(0)
        currentNode.set_color(yellow)
        g.draw(sc)

        # append closed node
        closed_set.append(currentNode)

        currentNode.set_color(blue)
        g.draw(sc)

        # Check if current node is goal
        if g.is_goal(currentNode):
            currentNode.set_color(purple)
            set_Color_Path(g, father, sc)
            return

        # list new neighbors
        newNeighbors = []
        for neighbor in g.get_neighbors(currentNode):
            if neighbor not in closed_set and neighbor not in open_set:
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    g.draw(sc)
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
    g.draw(sc)
    while open_set:

        # draw current node
        currentNode = open_set.pop(0)
        currentNode.set_color(yellow)
        g.draw(sc)

        # append closed node
        closed_set.append(currentNode)

        currentNode.set_color(blue)
        g.draw(sc)

        # Check if current node is goal
        if g.is_goal(currentNode):
            currentNode.set_color(purple)
            set_Color_Path(g, father, sc)
            return
        # list new neighbors
        newNeighbors = []
        for neighbor in g.get_neighbors(currentNode):
            if neighbor not in closed_set and neighbor not in open_set:
                newNeighbors.append(neighbor)
                father[neighbor.value] = currentNode.value
                if neighbor.value != g.goal.value:
                    neighbor.set_color(red)
                    g.draw(sc)

        # add list neighbors to open_set
        open_set.extend(newNeighbors)


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
