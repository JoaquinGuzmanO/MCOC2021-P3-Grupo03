import networkx as nx
import matplotlib.pyplot as plt

def tiempo (n1,n2,vel): #vel/tiemp
	pass

gris = "#7C7C7C"
verde = "#00701A"
cafe  = "#6C4E09"
G = nx.Graph()

#agregar nodos

G.add_node(0, pos=[1,2])
G.add_node(1, pos=[4,3])
G.add_node(2, pos=[1,6])
G.add_node(3, pos=[7,3])
G.add_node(4, pos=[10,1])
G.add_node(5, pos=[0,10])
G.add_node(6, pos=[4,0])
G.add_node(7, pos=[5,8])
G.add_node(8, pos=[9,7])
G.add_node(9, pos=[8,10])

#agregar arcos vel[km/hr]

G.add_edge(0,2, vel=120, color = gris)
G.add_edge(0,1, vel=40, color = cafe)
G.add_edge(0,6, vel=120, color = gris)
G.add_edge(1,2, vel=40, color = cafe)
G.add_edge(1,3, vel=60, color = verde)
G.add_edge(1,7, vel=40, color = cafe)
G.add_edge(2,5, vel=40, color = cafe)
G.add_edge(3,4, vel=60, color = verde)
G.add_edge(3,6, vel=40, color = cafe)
G.add_edge(3,7, vel=60, color = verde)
G.add_edge(3,8, vel=40, color = cafe)
G.add_edge(4,6, vel=120, color = gris)
G.add_edge(4,8, vel=120, color = gris)
G.add_edge(5,7, vel=120, color = gris)
G.add_edge(7,9, vel=60, color = verde)
G.add_edge(8,9, vel=60, color = verde)

pos = nx.get_node_attributes(G,"pos")
labels = nx.get_edge_attributes(G,"vel")
color = nx.get_edge_attributes(G,"color").values()


ax = plt.subplot()

plt.yticks([0,1,2,3,4,5,6,7,8,9,10],["0","1","2","3","4","5","6","7","8","9","10"])
plt.xticks([0,1,2,3,4,5,6,7,8,9,10],["0","1","2","3","4","5","6","7","8","9","10"])
plt.axis([-0.5, 10.5, -0.5, 10.5])
plt.ylabel("Y (Km)")
plt.xlabel("X (Km)")
plt.grid()

nx.draw(G, pos,edge_color=color,with_labels=True,width=2) #grafica la malla
ax.tick_params(labelleft=True, labelbottom=True)
plt.axis('on')
plt.show()

