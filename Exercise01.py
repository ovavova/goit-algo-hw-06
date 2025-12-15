""" Завдання 1

Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

info
📖 Реальну мережу можна вибрати на свій розсуд, якщо немає можливості придумати свою мережу, наближену до реальності.

Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).


Ідея: Станції київського метрополітену 

 """

import networkx as nx
import matplotlib.pyplot as plt

######## stations data 
# --- 1. Станції ---
nodes_list = [
    # Red Line
    "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska", 
    "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet", 
    "Teatralna", "Khreshchatyk", "Arsenalna", "Dnipro", "Hidropark", 
    "Livoberezhna", "Darnytsia", "Chernihivska", "Lisova",
    # Blue Line
    "Heroiv Dnipra", "Minska", "Obolon", "Pochaina", "Tarasa Shevchenka", 
    "Kontraktova Ploshcha", "Poshtova Ploshcha", "Maidan Nezalezhnosti", 
    "Ploshcha Ukrainskykh Heroiv", "Olimpiiska", "Palats 'Ukraina'", 
    "Lybidska", "Demiivska", "Holosiivska", "Vasylkivska", 
    "Vystavkovyi Tsentr", "Ipodrom", "Teremky",
    # Green Line
    "Syrets", "Dorohozhychi", "Lukianivska", "Zoloti Vorota", "Palats Sportu", 
    "Klovska", "Pecherska", "Zvirynetska", "Vydubychi", "Slavutych", 
    "Osokorky", "Pozniaky", "Kharkivska", "Vyrlytsia", "Boryspilska", 
    "Chervonyi Khutir"
]

# --- 2. EDGES (Station A, Station B, Weight, Label/Color) ---
edges_list = [
    # --- M1: Red Line ---
    ("Akademmistechko", "Zhytomyrska", 2, "red"),
    ("Zhytomyrska", "Sviatoshyn", 2, "red"),
    ("Sviatoshyn", "Nyvky", 2, "red"),
    ("Nyvky", "Beresteiska", 2, "red"),
    ("Beresteiska", "Shuliavska", 2, "red"),
    ("Shuliavska", "Politekhnichnyi Instytut", 2, "red"),
    ("Politekhnichnyi Instytut", "Vokzalna", 3, "red"),
    ("Vokzalna", "Universytet", 2, "red"),
    ("Universytet", "Teatralna", 2, "red"),
    ("Teatralna", "Khreshchatyk", 2, "red"),
    ("Khreshchatyk", "Arsenalna", 2, "red"),
    ("Arsenalna", "Dnipro", 3, "red"),
    ("Dnipro", "Hidropark", 3, "red"),
    ("Hidropark", "Livoberezhna", 3, "red"),
    ("Livoberezhna", "Darnytsia", 2, "red"),
    ("Darnytsia", "Chernihivska", 2, "red"),
    ("Chernihivska", "Lisova", 2, "red"),

    # --- M2: Blue Line ---
    ("Heroiv Dnipra", "Minska", 2, "blue"),
    ("Minska", "Obolon", 2, "blue"),
    ("Obolon", "Pochaina", 2, "blue"),
    ("Pochaina", "Tarasa Shevchenka", 2, "blue"),
    ("Tarasa Shevchenka", "Kontraktova Ploshcha", 2, "blue"),
    ("Kontraktova Ploshcha", "Poshtova Ploshcha", 2, "blue"),
    ("Poshtova Ploshcha", "Maidan Nezalezhnosti", 2, "blue"),
    ("Maidan Nezalezhnosti", "Ploshcha Ukrainskykh Heroiv", 2, "blue"),
    ("Ploshcha Ukrainskykh Heroiv", "Olimpiiska", 2, "blue"),
    ("Olimpiiska", "Palats 'Ukraina'", 2, "blue"),
    ("Palats 'Ukraina'", "Lybidska", 2, "blue"),
    ("Lybidska", "Demiivska", 2, "blue"),
    ("Demiivska", "Holosiivska", 2, "blue"),
    ("Holosiivska", "Vasylkivska", 2, "blue"),
    ("Vasylkivska", "Vystavkovyi Tsentr", 2, "blue"),
    ("Vystavkovyi Tsentr", "Ipodrom", 2, "blue"),
    ("Ipodrom", "Teremky", 2, "blue"),

    # --- M3: Green Line ---
    ("Syrets", "Dorohozhychi", 2, "green"),
    ("Dorohozhychi", "Lukianivska", 3, "green"),
    ("Lukianivska", "Zoloti Vorota", 3, "green"),
    ("Zoloti Vorota", "Palats Sportu", 2, "green"),
    ("Palats Sportu", "Klovska", 2, "green"),
    ("Klovska", "Pecherska", 2, "green"),
    ("Pecherska", "Zvirynetska", 2, "green"),
    ("Zvirynetska", "Vydubychi", 2, "green"),
    ("Vydubychi", "Slavutych", 4, "green"),
    ("Slavutych", "Osokorky", 2, "green"),
    ("Osokorky", "Pozniaky", 2, "green"),
    ("Pozniaky", "Kharkivska", 2, "green"),
    ("Kharkivska", "Vyrlytsia", 2, "green"),
    ("Vyrlytsia", "Boryspilska", 2, "green"),
    ("Boryspilska", "Chervonyi Khutir", 2, "green"),

    # --- Transfers (Static 7 mins) ---
    ("Teatralna", "Zoloti Vorota", 7, "purple"),             
    ("Khreshchatyk", "Maidan Nezalezhnosti", 7, "purple"),   
    ("Ploshcha Ukrainskykh Heroiv", "Palats Sportu", 7, "purple") 
]

def create_kyiv_metro_graph(nodes_list:list, edge_list: list):
    G = nx.Graph()

    # --- 3. Build Graph ---
    G.add_nodes_from(nodes_list)

    # 4. Build Nodes
    for station_a, station_b, travel_time, line_color in edge_list:
        G.add_edge(station_a, station_b, weight=travel_time, color=line_color)

    return G

# --- Analysis Function ---
def analyze_station(graph, station_name):
    """Simple helper to analyze a specific node"""
    if station_name in graph:
        degree = graph.degree[station_name]
        neighbors = list(graph.neighbors(station_name))
        print(f"\nAnalysis for '{station_name}':")
        print(f"- Connections (Degree): {degree}")
        print(f"- Neighbors: {neighbors}")
    else:
        return -1
    
G = create_kyiv_metro_graph(nodes_list, edges_list)

if __name__ == "__main__":

    # ---  Visualization ---


    print(f"Graph Created Successfully.")
    print(f"Nodes: {G.number_of_nodes()} | Edges: {G.number_of_edges()}")

    # Plotting
    plt.figure(figsize=(14, 10))

    # 1.  Layout!!!
    pos = nx.spring_layout(G, seed=13, k=0.3) 

    #pos = nx.kamada_kawai_layout(G) 

    #pos = nx.planar_layout(G) 

    #pos = nx.shell_layout(G) 

    #pos = nx.spectral_layout(G) 

    # 2. Get edge colors from the edge attributes
    edges = G.edges()
    edge_colors = [G[u][v]['color'] for u, v in edges]

    # Options for visualisation for nodes
    options_nodes = {
        "node_color": "lightgrey",
        "node_size": 250,
        "alpha": 0.9
    }

    # Options for visualisation for edges
    options_edges = {
        "edge_color": edge_colors,
        "width": 3,
        "alpha": 0.7
    }

    # 3. Draw
    # Draw Nodes (Grey by default to let edges pop)
    nx.draw_networkx_nodes(G, pos, **options_nodes)

    # Draw Edges (Using our line colors)
    nx.draw_networkx_edges(G, pos, **options_edges)

    # Draw Labels
    nx.draw_networkx_labels(G, pos, font_size=8)

    plt.title("Kyiv Metro Topology (Nodes & Weighted Edges)")
    plt.axis('off')
    plt.show()

    # Example analysis
    analyze_station(G, "Khreshchatyk")

    analyze_station(G, "Cheremky")