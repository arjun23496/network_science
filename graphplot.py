import pylab
import networkx as nx

def show_graph(aGraph):
	fig = pylab.figure()
	pylab.title(aGraph.name)
	pos = nx.spring_layout(aGraph)  
	nx.draw(aGraph, pos)
	fig.show()
	
def show_histogram(aGraph):		
	fig = pylab.figure()
	pylab.title(aGraph.name)
	hist = nx.degree_histogram(aGraph)
	pylab.bar(range(len(hist)), hist, align = 'center')
	pylab.xlim((0, len(hist)))
	pylab.xlabel("Degree of node")
	pylab.ylabel("Number of nodes")
	#pylab.show()
	fig.show()


def show_plots():
        pylab.show()
