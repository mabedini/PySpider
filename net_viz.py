import networkx as nx
import matplotlib.pyplot as plt
from general import *
import os


class web_graph :

  edges = set()
  nodes = {}
  fl_edges = ''
  fl_nodes = ''
  web_net_graph=nx.Graph()


  def __init__(self , project_name ):
    self.fl_edges = os.path.join(project_name,'edges.pkl')
    self.fl_nodes = os.path.join(project_name,'nodes.pkl')

    if os.path.isfile(self.fl_edges):
      self.edges = unpickle_obj(self.fl_edges)

    if os.path.isfile(self.fl_nodes):
      self.nodes = unpickle_obj(self.fl_nodes)

    #his.web_net_graph = nx.Graph()
    return


  def add_edge(self,pg1,pg2):
    if pg1 not in self.nodes:
      self.nodes[pg1] = len(self.nodes)
    if pg2 not in self.nodes:
      self.nodes[pg2] = len(self.nodes)

    if ((self.nodes[pg1] , self.nodes[pg2]) not in self.edges) and  ((self.nodes[pg2] , self.nodes[pg1]) not in self.edges) :
      self.edges.add((self.nodes[pg1] , self.nodes[pg2]))
      #nx.draw(self.web_net_graph)
      #plt.show()  # display
      #self.web_net_graph.add_node(self.nodes[pg1])
      #self.web_net_graph.add_node(self.nodes[pg2])

      self.web_net_graph.add_edge(self.nodes[pg1], self.nodes[pg2])
      #plt.savefig("web_viz.png")


  def Network_toFile(self):
    pickle_obj(self.edges,self.fl_edges)
    pickle_obj(self.nodes,self.fl_nodes)

  def draw_graph(self):
    nx.draw(self.web_net_graph, node_size=10  )
    plt.savefig("web_viz.png",bbox_inches='tight',dpi=100)  # save as png
    #plt.show()  # display