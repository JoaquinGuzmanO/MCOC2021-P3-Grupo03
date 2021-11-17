# MCOC2021-P3-Grupo03
Proyecto 3 "Evaluación de Américo Vespucio Oriente" Métodos Computacionales en Obras Civiles


# Integragntes:
- Joaquín Guzmán Ossandón
- Paula Villalobos Bradanovic
# P3 E4

 - Flujo en cada arco
 
![Flujo en cada arco](https://user-images.githubusercontent.com/62270417/142104249-58fc64e5-7a16-4b53-a5d7-f8205cecf0c7.PNG)
 
 - Costo de cada arco
 
![costo de cada arco](https://user-images.githubusercontent.com/62270417/142105026-6562b256-6f18-4ba4-889c-eac673a12909.PNG)

 - Funciones de costo de cada arco

![Funciones de costo por arco](https://user-images.githubusercontent.com/62270417/142105267-4953c21c-ba33-4b85-b7f4-0c797230c54b.PNG)

 - Error de cada arco, de forma de demostrar el cumplimiento del equilibrio de Wardrop
 
![errores](https://user-images.githubusercontent.com/62270417/142106140-e46d8981-1fad-430f-9b65-ed4ee2ebe757.PNG)
 
El qeuilibrio se consiguio a traves del suguinte codigo, el cual va iterando la matriz origen destino hasta lograr que los viajes entre zonas
sean iguales a 0 hasta que ya no exista una demanda actual.

```python
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
```
# P3 E3

 - Mapa Joaquín Guzmán 

![mapa_jg](https://user-images.githubusercontent.com/62270417/141528825-12caef80-ebe3-483f-8e33-6ad883e25e63.png)

 - Mapa Paula Villalobos 
 
![mapacomuna](https://user-images.githubusercontent.com/88356859/141600622-59998ad3-c7ea-4ea2-983d-0fdfda06ab91.png)


# P3 E2

![fig1](https://user-images.githubusercontent.com/88356859/141029666-03d98949-dbf3-4d84-ac68-05a3c32c2759.png)


 - Ruta 0 - 9

![fig2](https://user-images.githubusercontent.com/88356859/141029697-07e67359-218a-4133-9022-d15e11acf2e8.png)

 - Ruta 4 - 5

![fig3](https://user-images.githubusercontent.com/88356859/141029715-faea70ed-6975-4ddc-b259-7b1b59e4385f.png)

 - Ruta 0 - 4

![fig4](https://user-images.githubusercontent.com/88356859/141029738-1459f136-0feb-4d3a-9598-2c229892c7b2.png)


