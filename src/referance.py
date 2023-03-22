from os import TMP_MAX
from tracemalloc import start
from Space import *
from Constants import *


def check_Node(node: Node, arr: list[Node]):
    for i in range(0, len(arr)):
        if arr[i].value == node.value:
            return True
    return False


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


def BFS(g: Graph, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set: list[Node] = [g.start]
    closed_set: list[Node] = []
    father = [-1]*g.get_len()

    # TODO: Implement BFS algorithm using open_set, closed_set, and father
    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while len(open_set) != 0:
            N_current: Node = open_set[i]
        # Thay đổi màu cho nút đang xét
            N_current.set_color(yellow)
            g.draw(sc)
        # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(N_current):

                for i in father:
                    print(i)
                    print(" ")

                set_Color_Path(g, father, sc)
                return
        # xóa nút đã kiểm tra
            open_set.remove(N_current)
        # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(N_current)
        # Thay đổi màu cho nút đã được kiểm tra
            N_current.set_color(blue)
            g.draw(sc)
        # thêm các nút được thăm tới vào open_set
            neighbors: list[Node] = g.get_neighbors(N_current)
            while len(neighbors) != 0:
                if not check_Node(neighbors[0], closed_set):
                    if not check_Node(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        open_set.append(neighbors[0])
                        father[neighbors[0].value] = N_current.value
                neighbors.remove(neighbors[0])

    raise NotImplementedError('Not implemented')


def DFS(g: Graph, sc: pygame.Surface):
    print('Implement DFS algorithm')

    open_set: list[Node] = [g.start]
    closed_set: list[Node] = []
    father = [-1]*g.get_len()

    # TODO: Implement DFS algorithm using open_set, closed_set, and father
    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while len(open_set) != 0:
            N_current: Node = open_set[i]
            N_current.set_color(yellow)
            g.draw(sc)
        # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(N_current):
                set_Color_Path(g, father, sc)
                return
        # xóa nút đã kiểm tra
            open_set.remove(N_current)
        # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(N_current)
        # Thay đổi màu cho nút đã được kiểm tra
            N_current.set_color(blue)
            g.draw(sc)
        # thêm cái nút được thăm tới vào open_set
            neighbors: list[Node] = g.get_neighbors(N_current)
            temp: list[Node] = []
            while len(neighbors) != 0:
                if not check_Node(neighbors[0], closed_set):
                    if not check_Node(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        temp.append(neighbors[0])
                        father[neighbors[0].value] = N_current.value
                neighbors.remove(neighbors[0])
            open_set[0:0] = temp

    raise NotImplementedError('Not implemented')


def Min_Cost(g: Graph, open_set: list[Node], cost):
    min = g.get_len()
    temp = open_set[0]
    for i in open_set:
        if min > cost[i.value]:
            min = cost[i.value]
            temp = i
    return temp


def Min_Cost_Heuristic(g: Graph, open_set: list[Node], cost):
    min = 100000
    temp = open_set[0]
    for i in open_set:
        if min > cost[i.value] + g.heuristic(i):
            min = cost[i.value] + g.heuristic(i)
            temp = i
    return temp


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    open_set: list[Node] = [g.start]
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while len(open_set) != 0:
            N_current: Node = Min_Cost(g, open_set, cost)
            if N_current.value != g.start.value:
                N_current.set_color(yellow)
                g.draw(sc)
            # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(N_current):
                set_Color_Path(g, father, sc)
                return
            # xóa nút đã kiểm tra
            open_set.remove(N_current)
            # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(N_current)
            # Thay đổi màu cho nút đã được kiểm tra
            N_current.set_color(blue)
            g.draw(sc)
            # kiểm tra các biên và update cost
            neighbors: list[Node] = g.get_neighbors(N_current)
            while len(neighbors) != 0:
                if not check_Node(neighbors[0], closed_set):
                    if not check_Node(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        cost[neighbors[0].value] = cost[N_current.value] + \
                            g.Cost_two_Node(N_current, neighbors[0])
                        open_set.append(neighbors[0])
                        father[neighbors[0].value] = N_current.value
                neighbors.remove(neighbors[0])

    raise NotImplementedError('Not implemented')


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set: list[Node] = [g.start]
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while len(open_set) != 0:
            N_current: Node = Min_Cost_Heuristic(g, open_set, cost)
            if N_current.value != g.start.value:
                N_current.set_color(yellow)
                g.draw(sc)
            # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(N_current):
                set_Color_Path(g, father, sc)
                return
            # xóa nút đã kiểm tra
            open_set.remove(N_current)
            # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(N_current)
            # Thay đổi màu cho nút đã được kiểm tra
            N_current.set_color(blue)
            g.draw(sc)
            # kiểm tra các biên và update cost
            neighbors: list[Node] = g.get_neighbors(N_current)
            while len(neighbors) != 0:
                if not check_Node(neighbors[0], closed_set):
                    if not check_Node(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        cost[neighbors[0].value] = cost[N_current.value] + \
                            g.Cost_two_Node(N_current, neighbors[0])
                        open_set.append(neighbors[0])
                        father[neighbors[0].value] = N_current.value
                neighbors.remove(neighbors[0])

    raise NotImplementedError('Not implemented')