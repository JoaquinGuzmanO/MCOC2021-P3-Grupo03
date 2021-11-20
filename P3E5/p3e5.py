import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gps
import csv

zonas_gdf = gps.read_file("eod.json")
id_zonas_AVO = [590,146,684,683,666,682,677,306,287,307,288,291,289,304,290,266,269]
id_zonas_cercanas_AVO = [589,584,675,672,674,326,599,597,598,153,148,147,152,678,667,668,669,300,321,312,292,296,305,293,265,267,282,281,435,433,434,512,505,496,507,508,498,506,591,587]
zonas_AVO = zonas_gdf[zonas_gdf.ID.isin(id_zonas_AVO)]
zonas_cercanas_AVO = zonas_gdf[zonas_gdf.ID.isin(id_zonas_cercanas_AVO)]
id_zonas_destino_AVO = []

for i in range(len(id_zonas_AVO)):
    with open('mod.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            if int(row[1]) == id_zonas_AVO[i]:
                id_zonas_destino_AVO.append(int(row[0]))

for i in range(len(id_zonas_cercanas_AVO)):
    with open('mod.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            if int(row[1]) == id_zonas_cercanas_AVO[i]:
                id_zonas_destino_AVO.append(int(row[0]))
                
zonas_destino_AVO = zonas_gdf[zonas_gdf.ID.isin(list(set(id_zonas_destino_AVO)))]

all_id = id_zonas_destino_AVO + id_zonas_AVO + id_zonas_cercanas_AVO
all_id = list(set(all_id))
all_id.pop(all_id.index(816))
all_id.pop(all_id.index(827))
all_id.pop(all_id.index(727))
all_id.pop(all_id.index(754))
all_id.pop(all_id.index(328))
all_zonas = zonas_gdf[zonas_gdf.ID.isin(all_id)]
# centroid = all_zonas.centroid
ox.config(use_cache=True)

north = -33.34
south = -33.655
west = -70.9
east = -70.45

G = ox.graph_from_bbox(north, south, east, west, network_type="drive")
gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

gdf_cortado = gps.overlay(gdf_edges, all_zonas,"intersection")
gdf_cortado_AVO = gps.overlay(gdf_edges, zonas_AVO,"intersection")

gdf_motorway = gdf_cortado[gdf_cortado.highway=="motorway"]
gdf_secondary = gdf_cortado[gdf_cortado.highway=="secondary"]
gdf_tertiary = gdf_cortado[gdf_cortado.highway=="tertiary"]
gdf_primary = gdf_cortado[gdf_cortado.highway=="primary"]
gdf_AVO1 = gdf_cortado_AVO[gdf_cortado_AVO.name=="Avenida Ossa"]
gdf_AVO2 = gdf_cortado_AVO[gdf_cortado_AVO.name=="Avenida Américo Vespucio Sur"]
gdf_AVO3 = gdf_cortado_AVO[gdf_cortado_AVO.name=="Avenida Américo Vespucio Norte"]
gdf_AVO4 = gdf_cortado_AVO[gdf_cortado_AVO.name=="Avenida Américo Vespucio"]

#                 ####### GRAFICAR #######

fig, ax = plt.subplots(1,1)

all_zonas.plot(ax=ax,color="#CDCDCD")
# for idx,row in all_zonas.iterrows():
#     c=row.geometry.centroid
#     ax.annotate(text=row["ID"],xy=(c.x,c.y),horizontalalignment="center")
gdf_motorway.plot(ax=ax,color="orange",width=1)
gdf_primary.plot(ax=ax,color="yellow",width=0.8)
gdf_secondary.plot(ax=ax,color="green",width=0.5)
gdf_tertiary.plot(ax=ax,color="blue",width=1)

gdf_AVO1.plot(ax=ax,color="red")
gdf_AVO2.plot(ax=ax,color="red")
gdf_AVO3.plot(ax=ax,color="red")
gdf_AVO4.plot(ax=ax,color="red")

plt.title("Zonas influencia en AVO \n")

plt.show() 
File.close()