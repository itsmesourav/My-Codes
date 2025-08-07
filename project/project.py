import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edge("happy", "joyful")
G.add_edge("happy", "content")
nx.draw(G, with_labels=True)
plt.show()
