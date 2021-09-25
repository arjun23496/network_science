import networkx as nx 
import numpy as np

def make_simple_graph():
    g = nx.Graph(name="simple_graph")
    
    nodes = [ "A", "B", "C", "D", "E" ]
    
    edges = [
        ("A", "C"),
        ("A", "D"),
        ("A", "E"),
        ("E", "C"),
        ("E", "D"),
        ("B", "D")
        ]
        
    for node in nodes:
        g.add_node(node)
        
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    return g 


def compute_diameter_and_degrees(g):
    degrees = []    
    for node in g.nodes():
        degrees.append(g.degree(node))
    
    return nx.diameter(g), degrees


def avg_degree(g):
    degrees = []    
    for node in g.nodes():
        degrees.append(g.degree(node))
    
    return np.mean(degrees)
    

def get_centers(g):
    return nx.center(g)


def get_widest_graph(n_nodes=5):
    g = nx.Graph(name="widest_graph")
    nodes = list(range(5))
    
    for node in nodes:
        
    
