import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gps

zonas_gdf = gps.read_file("eod.json")
id_all_zonas = [293,292,296,295,303,305,269,265,270,322]
id_zonas_interes_borde = [292,296,295,303,305,269,265,270,322]
id_zona_central = 293
all_zonas = zonas_gdf[zonas_gdf.ID.isin(id_all_zonas)]
zonas_seleccionadas_borde = zonas_gdf[zonas_gdf.ID.isin(id_zonas_interes_borde)]
zona_central = zonas_gdf[zonas_gdf.ID == id_zona_central]

ox.config(use_cache=True)

north = -33.405
south = -33.445
west = -70.580
east = -70.535

G = ox.graph_from_bbox(north, south, east, west, network_type="drive")
gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

gdf_cortado = gps.clip(gdf_edges, all_zonas)

gdf_motorway = gdf_cortado[gdf_cortado.highway=="motorway"]
gdf_secondary = gdf_cortado[gdf_cortado.highway=="secondary"]
gdf_tertiary = gdf_cortado[gdf_cortado.highway=="tertiary"]
gdf_primary = gdf_cortado[gdf_cortado.highway=="primary"]
gdf_residential = gdf_cortado[gdf_cortado.highway=="residential"]

                ####### GRAFICAR #######

fig, ax = plt.subplots(1,1)
zonas_seleccionadas_borde.plot(ax=ax,color="#CDCDCD")
zona_central.plot(ax=ax,color="#FFB2B2")
gdf_motorway.plot(ax=ax,color="red")
gdf_secondary.plot(ax=ax,color="yellow")
gdf_tertiary.plot(ax=ax,color="blue")
gdf_primary.plot(ax=ax,color="green")
gdf_residential.plot(ax=ax,color="black")

plt.title("Zona Las Condes: [293] vecinas: [292,296,295,303,305,269,265,270,322]\n")

plt.show()



