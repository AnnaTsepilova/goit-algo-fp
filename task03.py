import heapq


# Клас для представлення графа
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  


# Алгоритм Дейкстри
def dijkstra(graph, start):
    # Відстань від стартової вершини до кожної іншої вершини 
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Мінімальна купа для вибору вершини з найменшою відстанню
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдена відстань більша за поточну відстань, продовжуємо 
        if current_distance > distances[current_vertex]:
            continue

        # Перевірка всіх сусідів поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Якщо знайдена коротша відстань, оновлюємо
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Приклад використання
def main():
    g = Graph(5)  # Створюємо граф з 5 вершинами
    g.add_edge(0, 1, 10)
    g.add_edge(0, 4, 5)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 4, 2)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 4, 7)

    # Виклик алгоритму Дейкстри
    start_vertex = 0
    distances = dijkstra(g.graph, start_vertex)

    # Виведення найкоротших шляхів від початкової вершини
    for vertex, distance in distances.items():
        print(f"Відстань від вершини {start_vertex} до вершини {vertex}: {distance}")


if __name__ == "__main__":
    main()
