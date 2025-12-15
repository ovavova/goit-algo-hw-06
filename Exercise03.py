""" Завдання 3

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа. """



import networkx as nx
import matplotlib.pyplot as plt
import Exercise01

G = Exercise01.G

if __name__ == "__main__":
    print("Алгоритм Дейкстри – найкоротші шляхи між усіма вершинами\n")

    for source in G.nodes():
        lengths, paths = nx.single_source_dijkstra(G, source=source, weight="weight")
        print(f"Від вершини '{source}':")
        for target in G.nodes():
            if target != source:
                print(
                    f"  -> до '{target}': шлях {paths[target]}, довжина {lengths[target]:.2f}"
                )
        print()