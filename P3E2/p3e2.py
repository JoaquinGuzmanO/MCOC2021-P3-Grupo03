import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import dijkstra_path

#colores 

gris = "#7C7C7C"
verde = "#00701A"
cafe  = "#6C4E09"


def tiempo(pos_1, pos_2, vel):

    x1, y1 = pos_1
    x2, y2 = pos_2
    dx = x1 - x2
    dy = y1 - y2
    dist = (dx**2 + dy**2)**(1/2)
    t = dist/vel
    return t


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

G.add_edge(0,2, vel = 120, weigth = tiempo([1,2], [1,6], 120), color = gris)
G.add_edge(0,1, vel = 40, weigth = tiempo([1,2], [4,3], 40), color = cafe)
G.add_edge(0,6, vel = 120, weigth = tiempo([1,2], [4,0], 120), color = gris)
G.add_edge(1,2, vel = 40, weigth = tiempo([4,3], [1,6], 40), color = cafe)
G.add_edge(1,3, vel = 60, weigth = tiempo([4,3], [7,3], 60), color = verde)
G.add_edge(1,7, vel = 40, weigth = tiempo([4,3], [5,8], 40), color = cafe)
G.add_edge(2,5, vel = 40, weigth = tiempo([1,6], [0,10], 40), color = cafe)
G.add_edge(3,4, vel = 60, weigth = tiempo([7,3], [10,1], 60), color = verde)
G.add_edge(3,6, vel = 40, weigth = tiempo([7,3], [4,0], 40), color = cafe)
G.add_edge(3,7, vel = 60, weigth = tiempo([7,3], [5,8], 60), color = verde)
G.add_edge(3,8, vel = 40, weigth = tiempo([7,3], [9,7], 40), color = cafe)
G.add_edge(4,6, vel = 120, weigth = tiempo([10,1], [4,0], 120), color = gris)
G.add_edge(4,8, vel = 120, weigth = tiempo([10,1], [9,7], 120), color = gris)
G.add_edge(5,7, vel = 120, weigth = tiempo([0,10], [5,8], 120), color = gris)
G.add_edge(7,9, vel = 60, weigth = tiempo([5,8], [8,10], 60), color = verde)
G.add_edge(8,9, vel = 60, weigth = tiempo([9,7], [8,10], 60), color = verde)


pos = nx.get_node_attributes(G,"pos")
labels = nx.get_edge_attributes(G,"weigth")
color = nx.get_edge_attributes(G,"color").values()


#Rutas minimas

ruta09 = dijkstra_path(G,0,9, "weigth")
ruta45 = dijkstra_path(G,4,5, "weigth")
ruta04 = dijkstra_path(G,0,4, "weigth")


#Tiempo total ruta 0 - 9

tiempo_ruta09 = 0
Nparadas = len(ruta09)

print(f"Ruta Nparadas={Nparadas} ruta 0 - 9: {ruta09}")

for i in range(Nparadas-1):
	parada_i = ruta09[i]
	parada_f = ruta09[i+1]
	tiempo_tramo_i = G.edges[parada_i, parada_f]["weigth"]
	print(f"Tramo {i}  {parada_i} a {parada_f} tiempo={tiempo_tramo_i}")
	tiempo_ruta09 += tiempo_tramo_i

print(f"Tiempo de ruta = {tiempo_ruta09}")


#Tiempo total ruta 4 - 5

tiempo_ruta45 = 0
Nparadas = len(ruta45)

print(f"Ruta Nparadas={Nparadas} ruta 0 - 9: {ruta45}")

for i in range(Nparadas-1):
	parada_i = ruta45[i]
	parada_f = ruta45[i+1]
	tiempo_tramo_i = G.edges[parada_i, parada_f]["weigth"]
	print(f"Tramo {i}  {parada_i} a {parada_f} tiempo={tiempo_tramo_i}")
	tiempo_ruta45 += tiempo_tramo_i

print(f"Tiempo de ruta = {tiempo_ruta45}")

#Tiempo total ruta 0 - 4

tiempo_ruta04 = 0
Nparadas = len(ruta04)

print(f"Ruta Nparadas={Nparadas} ruta 0 - 9: {ruta04}")

for i in range(Nparadas-1):
	parada_i = ruta04[i]
	parada_f = ruta04[i+1]
	tiempo_tramo_i = G.edges[parada_i, parada_f]["weigth"]
	print(f"Tramo {i}  {parada_i} a {parada_f} tiempo={tiempo_tramo_i}")
	tiempo_ruta04 += tiempo_tramo_i

print(f"Tiempo de ruta = {tiempo_ruta04}")

plt.figure(1)

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



#grafcar ruta minima para 0-9

color09 = []

for ni, nf in G.edges:
	if ni in ruta09 and nf in ruta09:
		color09.append("r")
	else:
		color09.append(gris)
	

plt.figure(2)

ax = plt.subplot()

plt.yticks([0,1,2,3,4,5,6,7,8,9,10],["0","1","2","3","4","5","6","7","8","9","10"])
plt.xticks([0,1,2,3,4,5,6,7,8,9,10],["0","1","2","3","4","5","6","7","8","9","10"])
plt.axis([-0.5, 10.5, -0.5, 10.5])
plt.ylabel("Y (Km)")
plt.xlabel("X (Km)")
plt.grid()
plt.suptitle(f"Ruta minima: {ruta09} - Tiempo: {tiempo_ruta09}")

nx.draw(G, pos,edge_color=color09,with_labels=True,width=2) #grafica la malla
ax.tick_params(labelleft=True, labelbottom=True)
plt.axis('on')
plt.show()

plt.show()



#grafcar ruta minima para 4-5

color45 = []

for ni, nf in G.edges:
	if ni in ruta45 and nf in ruta45:
		color45.append("r")
	else:
		color45.append(gris)
	

plt.figure(3)

ax = plt.subplot()

plt.yticks([0,1,2,3,4,5,6,7,8,9,10],["0","1","2","3","4","5","6","7","8","9","10"])
plt.xticks([0,1,2,3,4,5,6,7,8,9,10],["0","1","2","3","4","5","6","7","8","9","10"])
plt.axis([-0.5, 10.5, -0.5, 10.5])
plt.ylabel("Y (Km)")
plt.xlabel("X (Km)")
plt.grid()
plt.suptitle(f"Ruta minima: {ruta45} - Tiempo: {tiempo_ruta45}")

nx.draw(G, pos,edge_color=color45,with_labels=True,width=2) #grafica la malla
ax.tick_params(labelleft=True, labelbottom=True)
plt.axis('on')
plt.show()

plt.show()



#grafcar ruta minima para 0-4

color04 = []

for ni, nf in G.edges:
	if ni in ruta04 and nf in ruta04:
		color04.append("r")
	else:
		color04.append(gris)
	

plt.figure(4)

ax = plt.subplot()

plt.yticks([0,1,2,3,4,5,6,7,8,9,10],["0","1","2","3","4","5","6","7","8","9","10"])
plt.xticks([0,1,2,3,4,5,6,7,8,9,10],["0","1","2","3","4","5","6","7","8","9","10"])
plt.axis([-0.5, 10.5, -0.5, 10.5])
plt.ylabel("Y (Km)")
plt.xlabel("X (Km)")
plt.grid()
plt.suptitle(f"Ruta minima: {ruta04} - Tiempo: {tiempo_ruta04}")

nx.draw(G, pos,edge_color=color04,with_labels=True,width=2) #grafica la malla
ax.tick_params(labelleft=True, labelbottom=True)
plt.axis('on')
plt.show()

plt.show()
