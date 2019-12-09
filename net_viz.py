import networkx as nx
import matplotlib.pyplot as plt


class web_graph :

  edges = set()
  nodes = {}

  web_net_graph=nx.Graph()


  def __init__(self ):
    #his.web_net_graph = nx.Graph()
    return


  def add_edge(self,pg1,pg2):
    if pg1 not in self.nodes:
      self.nodes[pg1] = len(self.nodes)
    if pg2 not in self.nodes:
      self.nodes[pg2] = len(self.nodes)

    if ((self.nodes[pg1] , self.nodes[pg2]) not in self.edges) and  ((self.nodes[pg2] , self.nodes[pg1]) not in self.edges) :
      self.edges.add((self.nodes[pg1] , self.nodes[pg2]))
      nx.draw(self.web_net_graph)
      plt.savefig("simple_path.png")
      #plt.show()  # display

      self.web_net_graph.add_edge(self.nodes[pg1], self.nodes[pg2])

  def draw_graph(self):
    nx.draw(self.web_net_graph)
    plt.savefig("simple_path.png")  # save as png
    plt.show()  # display