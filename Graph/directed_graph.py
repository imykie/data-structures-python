class Node:
    def __init__(self, data, adjacencies: list['Node'] = []) -> None:
        self.data = data
        self.adjacencies = adjacencies

    def connect(self, node: 'Node') -> None:
        self.adjacencies.append(node)

    def is_adjacent(self, node: 'Node') -> bool:
        for adjacency in self.adjacencies:
            if node == adjacency:
                return True
        return False


class DirectedGraph:
    def __init__(self) -> None:
        pass
