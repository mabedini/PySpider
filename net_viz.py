import networkx as nx
import matplotlib.pyplot as plt
import pickle
import os


class web_graph :

  edges = set()
  nodes = {}

  web_net_graph=nx.Graph()


  def __init__(self ):
    if os.path.isfile('edges.pkl'):
      self.edges = self.unpickle_obj('edges.pkl')

    if os.path.isfile('nodes.pkl'):
      self.nodes = self.unpickle_obj('nodes.pkl')

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

  def pickle_obj(self, data, flname):
    # open a file, where you ant to store the data
    file = open(flname, 'wb')
    # dump information to that file
    pickle.dump(data, file)
    # close the file
    file.close()

  def unpickle_obj(self, flname):
    # open a file, where you stored the pickled data
    file = open(flname, 'rb')
    tmpObj = pickle.load(file)
    # close the file
    file.close()
    return tmpObj


  def Network_toFile(self):
    self.pickle_obj(self.edges,'edges.pkl')
    self.pickle_obj(self.nodes,'nodes.pkl')

  def draw_graph(self):
    nx.draw(self.web_net_graph, node_size=10  )
    plt.savefig("web_viz.png",bbox_inches='tight',dpi=100)  # save as png
    #plt.show()  # display