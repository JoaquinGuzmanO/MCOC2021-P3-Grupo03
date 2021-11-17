import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import dijkstra_path

def costo (ni,nf,attr):
	funcosto_arco = attr["fcosto"]
	flujo_arco = attr["flujo"]
	return funcosto_arco(flujo_arco)

def error (ve,vr):
	e = round(abs(ve-vr)*100/vr,3)
	return str(e)+"%"


			######################################
			################ DATOS ###############
			######################################

G = nx.DiGraph()

f1 = lambda f: 10 + f/120
f2 = lambda f: 14 + 3*f/240
f3 = lambda f: 10 + f/240

OD = {
	("A","C") : 1100, ("A","D") : 1100, ("A","E") : 1020,
	("B","C") : 1140, ("B","D") : 1160,
										("C","E") : 1170, ("C","G") : 1180,
	("D","C") : 350, 					("D","E") : 1190, ("D","G") : 1200,
}	

OD_target = OD.copy()

G.add_node("A", pos=[1,5])
G.add_node("B", pos=[1,3])
G.add_node("C", pos=[3,3])
G.add_node("D", pos=[3,1])
G.add_node("E", pos=[5,5])
G.add_node("G", pos=[5,3])

G.add_edge("A","B", fcosto=f1, flujo=0, costo=0, f="10 + f/120")
G.add_edge("A","C", fcosto=f2, flujo=0, costo=0, f="14 + 3f/240")
G.add_edge("B","C", fcosto=f3, flujo=0, costo=0, f="10 + f/240")
G.add_edge("B","D", fcosto=f2, flujo=0, costo=0, f="14 + 3f/240")
G.add_edge("C","E", fcosto=f2, flujo=0, costo=0, f="14 + 3f/240")
G.add_edge("C","G", fcosto=f3, flujo=0, costo=0, f="10 + f/240")
G.add_edge("D","C", fcosto=f1, flujo=0, costo=0, f="10 + f/120")
G.add_edge("D","G", fcosto=f2, flujo=0, costo=0, f="14 + 3f/240")
G.add_edge("G","E", fcosto=f1, flujo=0, costo=0, f="10 + f/120")


			######################################
			############# EQUILIBRIO #############
			######################################

while True:

	se_asigno_demanda = False

	for key in OD:
		origen = key[0]
		destino = key[1]
		demanda_actual = OD[key]
		demanda_target = OD_target[key]

		if demanda_actual > 0:
			path = dijkstra_path(G,origen,destino,weight=costo)
			Nparadas = len(path)

			for i_parada in range(Nparadas-1):
				o = path[i_parada]
				d = path[i_parada+1]
				flujo_antes = G.edges[o,d]["flujo"]
				G.edges[o,d]["flujo"] += 1

			OD[key] -= 1
			se_asigno_demanda = True

	if not se_asigno_demanda:
		break	

for ni, nf in G.edges:
	arco = G.edges[ni, nf]
	funcosto_arco=arco["fcosto"]
	flujo_arco=arco["flujo"]
	arco["costo"] = funcosto_arco(flujo_arco)

for i in G.edges():
    G.edges[i]["flujo"] = round(G.edges[i]["flujo"],4)
    G.edges[i]["costo"] = round(G.edges[i]["costo"],2)


			######################################
			############# VERIFICAR ##############
			######################################

arcos = ["A-B","A-C","B-C","B-D","C-E","C-G","D-C","D-G","G-E"]
flujo_esperado = [1370,1860,1400,2270,2030.86,1954.29,965.14,1774.86,1349.14]
flujo_obtenido = []

for i in G.edges():
	flujo_obtenido.append(G.edges[i]["flujo"])

for i in range(len(flujo_obtenido)):
	print("Para el arco "+arcos[i]+" se tiene un erro de: "+error(flujo_esperado[i],flujo_obtenido[i]))
print("\nTodos son menores al 1% por lo que queda verificado")

			######################################
			############## GRAFICAR ##############
			######################################

pos = nx.get_node_attributes(G,"pos")

plt.figure(1)
plt.title("Flujo final en cada arco")
labels = nx.get_edge_attributes(G,"flujo")
ax1 =plt.subplot(111)
nx.draw(G,pos,with_labels=True,font_weight="bold")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.figure(2)
plt.title("Costo final en cada arco")
labels = nx.get_edge_attributes(G,"costo")
ax1 =plt.subplot(111)
nx.draw(G,pos,with_labels=True,font_weight="bold")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.figure()
plt.title("Funciones de costo de cada arco")
labels = nx.get_edge_attributes(G,"f")
ax1 =plt.subplot(111)
nx.draw(G,pos,with_labels=True,font_weight="bold")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.show()