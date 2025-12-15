""" Завдання 2

Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі. 


Різниця отриманих шляхів в алгоритмах DFS та BFS для цього прикладу починаючи зі станції Контрактова полоща показує як DFS йде в "глиб" лінії відносно початкової станції, в той час як BFS зупиняється на синій вітці на Почайній - не доходячи до кінцевої і продовжує обхід з майдана незалежності по іншим гілкам до "виравнюючи" глибину обходу.

"""

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import Exercise01

### Converting NX Graph to dict of lists format - nodes -keys - list - neighbors to use manual DFS and BFS
def get_graph_dictionary(nx_graph):
    return nx.to_dict_of_lists(nx_graph)

### DFS ###
def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    traversal_order = []  # To record the order of visitation
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))
            # adding as we go for visual
            traversal_order.append(vertex)
    return traversal_order # for visual

### BFS ###

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    # for visual
    traversal_order = []


    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
            traversal_order.append(vertex)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return traversal_order  

###############


def visualize_single_traversal(nx_graph, traversal_order, title_text):
    """
    Plots the graph and labels nodes with their visitation order in bold red.
    """
    plt.figure(figsize=(12, 8))
    
    # 1. Calculate Layout (fixed seed keeps nodes in same place between plots)
    pos = nx.spring_layout(nx_graph, seed=13, k=0.4)

    # 2. Draw basic graph structure (neutral colors)
    edges = nx_graph.edges()
    edge_colors = [G[u][v]['color'] for u, v in edges]

    options_edges = {
    "edge_color": edge_colors,
    "width": 3,
    "alpha": 0.7
    }
    nx.draw_networkx_edges(nx_graph, pos, **options_edges)
    nx.draw_networkx_nodes(nx_graph, pos, node_color='grey', node_size=250)

    # 3. Create custom labels showing the order
    # Map node name to its order index (start from 1)
    # {NodeName: 1, NextNode: 2, ...}
    order_map = {node: i + 1 for i, node in enumerate(traversal_order)}
    
    custom_labels = {}
    for node in nx_graph.nodes():
        if node in order_map:
            # Add order number in parentheses below name
            custom_labels[node] = f"{node}\n({order_map[node]})"
        else:
            # Fallback for unreachable nodes if any
            custom_labels[node] = node

    # 4. Draw 
    # 
    nx.draw_networkx_labels(
        nx_graph, 
        pos, 
        labels=custom_labels, 
        font_size=8, 
        font_color='black',
    )
    


    plt.title(title_text, fontsize=15)
    plt.axis('off') # Turn off axis box
    plt.tight_layout()
    plt.show()


# --- Main Execution ---
if __name__ == "__main__":
    # Get the NetworkX graph object
    G = Exercise01.G
    # Get the dictionary format required by your algorithms
    subway_graph_dict = nx.to_dict_of_lists(G)

    # Pick a starting node dynamically (e.g., the first one found)
    start_node = "Kontraktova Ploshcha"  # Akademmistechko

        
    print(f"--- Starting route from node: {start_node} ---\n")

    # 1. Run and Visualize DFS
    dfs_result_path = dfs_iterative(subway_graph_dict, start_node)
    print(f"DFS Text Path View: {dfs_result_path}")
    visualize_single_traversal(G, dfs_result_path, "DFS Traversal Order (Step Number)")

    print("-" * 30 + "\n")

    # 2. Run and Visualize BFS
    bfs_result_path = bfs_iterative(subway_graph_dict, start_node)
    print(f"BFS Text Path View: {bfs_result_path}")
    visualize_single_traversal(G, bfs_result_path, "BFS Traversal Order (Strep Number)")

    print("\nFinished.")