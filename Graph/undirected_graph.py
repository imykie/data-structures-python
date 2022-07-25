from collections import defaultdict, deque
from typing import List


class Node:
    def __init__(self, data, adjacencies: List['Node'] = []) -> None:
        self.data = data
        self.adjacencies = adjacencies

    def connect(self, node: 'Node') -> None:
        self.adjacencies.append(node)
        node.adjacencies.append(self)

    def is_adjacent(self, node: 'Node') -> bool:
        for adjacency in self.adjacencies:
            if node == adjacency:
                return True
        return False


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add(self, node, adjacency) -> None:
        self.graph[node].append(adjacency)

    def bfs(self, start: 'Node', end: 'Node' = None):
        path = []
        queue = deque([start])
        visited = set()
        visited.add(start)

        while queue:
            node = queue.popleft()
            path.append(node.data)

            if end and node == end:
                return path

            if node.adjacencies:
                for adjacency in node.adjacencies:
                    if adjacency not in visited:
                        visited.add(adjacency)
                        queue.append(adjacency)

        return path

    def dfs(self, start: 'Node', end: 'Node' = None):
        visited = set()
        path = []

        def helper(node: 'Node'):
            if not node:
                return node

            visited.add(node)

            if node == end:
                return

            path.append(node.data)

            if node.adjacencies:
                for adjacency in node.adjacencies:
                    if adjacency not in visited:
                        return helper(adjacency)

        helper(start)
        return path

    def dfs_iterative(self, start: 'Node', end: 'Node' = None):
        path = []
        stack = deque([start])
        visited = set()
        visited.add(start)

        while stack:
            node = stack.pop()
            path.append(node.data)

            if end and node == end:
                break

            if node.adjacencies:
                for adjacency in node.adjacencies:
                    if adjacency not in visited:
                        visited.add(adjacency)
                        stack.append(adjacency)

        return path

    def shortest_path(self, start: 'Node', end: 'Node'):
        pass

    def djisktra(self, start: 'Node', end: 'Node'):
        pass

    def a_star(self, start: 'Node', end: 'Node'):
        pass


if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    m = Node('M')
    n = Node('N')
    y = Node('Y')
    z = Node('Z')
    a.connect(z)
    a.connect(m)
    b.connect(m)
    m.connect(n)
    y.connect(a)
    z.connect(n)
    y.connect(b)

    g = Graph()
    print(g.dfs(a, y))

