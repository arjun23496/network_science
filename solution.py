import networkx as nx
import numpy as np
import graphplot
import matplotlib.pyplot as plt

# Problem 1
def make_simple_graph():

    g = nx.Graph(name="simple_graph")

    nodes = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "D"),
        ("A", "E"),
        ("A", "C"),
        ("E", "D"),
        ("E", "C"),
        ("B", "D")
    ]

    for node in nodes:
        g.add_node(node)

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    return g


# Problem 2
def diameter_and_degrees(g):
    return nx.diameter(g), g.degree()


# Problem 3
def avg_degree(g):
    degree_dict = dict(g.degree())
    return np.mean([ val for key, val in degree_dict.items() ])


# Problem 4
def get_centers(g):
    return nx.center(g)

# Problem 5a
def get_widest_graph():
    nodes = ["0", "1", "2", "3", "4"]

    #edges for widest graph
    edges = [
            ("0", "1"),
            ("1", "2"),
            ("2", "3"),
            ("3", "4")
            ]
    g = nx.Graph(name="widest_graph")

    for node in nodes:
        g.add_node(node)

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    return g


def get_narrowest_graph():
    nodes = ["0", "1", "2", "3", "4"]
    edges = []
    g = nx.Graph(name="narrowest_graph")
    for nodei in nodes:
        for nodej in nodes:
            if nodei != nodej:
                edges.append((nodei, nodej))

    for node in nodes:
        g.add_node(node)

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    return g


def make_simple_cycle(N):
    nodes = list(range(N))
    
    edges = []

    for node in nodes:
        edges.append((node, (node+1)%N))

    g = nx.Graph(name="simple_cycle")
    for node in nodes:
        g.add_node(node)
    
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    return g


def make_complete_graph(N):
    nodes = list(range(N))
    
    edges = []

    for nodei in nodes:
        for nodej in nodes:
            edges.append((nodei, nodej))

    g = nx.Graph(name="complete_graph")
    for node in nodes:
        g.add_node(node)
    
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    return g


def make_binomial_graph(N, prob):
    nodes = list(range(N))
    
    edges = []

    for nodei in nodes:
        for nodej in nodes:
            toss = np.random.rand()
            if toss < prob:
                edges.append((nodei, nodej))

    g = nx.Graph(name="binomial_graph")
    for node in nodes:
        g.add_node(node)
    
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    return g


def show_binomial_graph_components(N,prob):  
    bgraph = make_binomial_graph(N,prob)
    i = 0
    subgraphs = [bgraph.subgraph(c) for c in nx.connected_components(bgraph)]
    for g in subgraphs:
        g.name = "Component " + str(i)
        graphplot.show_graph(g)
        i = i + 1


def optimal_city(g):
    nodes = g.nodes()
    min_avg = None
    min_node = None
    for node in nodes:
        shortest_path_lengths = nx.single_source_shortest_path_length(g, node)
        avg_pathlen = np.mean([ pathlen for key, pathlen in shortest_path_lengths.items() ])

        if min_avg is None or min_avg > avg_pathlen:
            min_node = node
            min_avg = avg_pathlen

    return min_node, min_avg


def make_airline_route_map():
    routemap =  [('St. Louis', 'Miami'), ('St. Louis', 'San Diego'), ('St. Louis', 'Chicago'), ('San Diego', 'Chicago'), ('San Diego', 'San Francisco'), ('San Diego', 'Minneapolis'), ('San Diego', 'Boston'), ('San Diego', 'Portland'), ('San Diego', 'Seattle'), ('Tulsa', 'New York'), ('Tulsa', 'Dallas'), ('Phoenix', 'Cleveland'), ('Phoenix', 'Denver'), ('Phoenix', 'Dallas'), ('Chicago', 'New York'), ('Chicago', 'Los Angeles'), ('Miami', 'New York'), ('Miami', 'Philadelphia'), ('Miami', 'Denver'), ('Boston', 'Atlanta'), ('Dallas', 'Cleveland'), ('Dallas', 'Albuquerque'), ('Philadelphia', 'Atlanta'), ('Denver', 'Minneapolis'), ('Denver', 'Cleveland'), ('Albuquerque', 'Atlanta'), ('Minneapolis', 'Portland'), ('Los Angeles', 'Seattle'), ('San Francisco', 'Portland'), ('San Francisco', 'Seattle'), ('San Francisco', 'Cleveland'), ('Seattle', 'Portland')]
    
    g = nx.Graph(name="airline_route")

    for edge in routemap:
        g.add_node(edge[0])
        g.add_node(edge[1])
        g.add_edge(edge[0], edge[1])

    return g


print("Problem 1:")
g = make_simple_graph()
print("graph created")
print("Problem 2: ", diameter_and_degrees(g))
print("Problem 3: ", avg_degree(g))
print("Problem4: ", get_centers(g))

print("Problem 5a")
widest_g = get_widest_graph()
print("diameter: ", diameter_and_degrees(widest_g)[0])
print("centers: ", get_centers(widest_g))

print("Problem 5b")
narrowest_g = get_narrowest_graph()
print("diameter: ", diameter_and_degrees(narrowest_g)[0])
print("centers: ", get_centers(narrowest_g))

print("Problem 5c")
simple_cycle_g = make_simple_cycle(5)
print("diameter: ", diameter_and_degrees(simple_cycle_g)[0])
print("centers: ", get_centers(simple_cycle_g))

print("Problem 5d")
complete_graph_g = make_complete_graph(5)
print("diameter: ", diameter_and_degrees(complete_graph_g)[0])
print("centers: ", get_centers(complete_graph_g))

print("Problem 5e")
for prob in np.arange(0.005, 0.051, 0.001):
    print("prob: {}".format(prob))
    show_binomial_graph_components(100, prob)
    plt.show()

print("Problem 6")
airline_route_g = make_airline_route_map()
graphplot.show_graph(airline_route_g)
plt.show()

print("Maximum number of hops taken by any passenger: ", diameter_and_degrees(airline_route_g)[0])
optimal_city_result = optimal_city(airline_route_g)
print("Optimal city for a rich jet-setter: {} min avg_pathlen: {}".format(optimal_city_result[0], optimal_city_result[1]))

print("Problem 6 - Er graph")
print("N=101, p=0.1")
configurations = [
        (101, 0.1),
        (101, 0.01),
        (101, 0.08)
        ]

for configuration in configurations:
    print("ER graph n: {} p:{}".format(configuration[0], configuration[1]))
    er1 = nx.erdos_renyi_graph(configuration[0], configuration[1])
    print("average degree: {}".format(avg_degree(er1)))
    graphplot.show_graph(er1)
    plt.show()

