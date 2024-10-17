import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors_map):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [colors_map.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Генерує n кольорів від темних до світлих відтінків
def generate_colors(n):
    return list(mcolors.LinearSegmentedColormap.from_list("", ["#00008B", "#ADD8E6"])(i/n) for i in range(n))


# Обхід в глибину з використанням стека
def dfs(tree_root):
    stack = [tree_root]
    visited = []
    order = []

    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            order.append(node)
            # Спочатку правий, потім лівий (щоб лівий вийшов першим)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return order


# Обхід в ширину з використанням черги
def bfs(tree_root):
    queue = deque([tree_root])
    visited = []
    order = []

    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.append(node)
            order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return order


# Візуалізує обхід дерева з унікальними кольорами для кожного вузла
def render_tree_walk(tree_root, visit_order):
    colors = generate_colors(len(visit_order))
    colors_map = {node.id: mcolors.to_hex(colors[i]) for i, node in enumerate(visit_order)}
    draw_tree(tree_root, colors_map)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходу в глибину (DFS)
dfs_order = dfs(root)
render_tree_walk(root, dfs_order)

# Візуалізація обходу в ширину (BFS)
bfs_order = bfs(root)
render_tree_walk(root, bfs_order)
