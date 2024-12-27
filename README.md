# Vehiculos-electricos
Uso de vehículos eléctricos
Este proyecto analiza la adopción de vehículos eléctricos (EV) en diferentes condados a lo largo del tiempo utilizando un enfoque basado en análisis exploratorio de datos (EDA), visualización y agrupamiento (
Objetivo
Comprender las tendencias de adopción de vehículos eléctricos y no eléctricos, identificar patrones por condado y año, y analizar cómo diferentes factores influyen en esta ado
Fases del Proyecto
1. Preparación de datos
Carga y limpieza de datos:
Se carga el conjunto de datos histórico sobre el tamaño de la población de vehículos eléctri
Se corr
Creación de columnas temporales:
Se
2. Análisis exploratorio (EDA)
Estadísticas descriptivas:
Identificación de proporciones de vehículos eléctricos y no eléctricos en diferentes condados.
Agrupamiento por condado y año:
Se calcula el ratio de vehículos eléctricos para cada condado y año, permitiendo identificar las regiones con mayor adopción.
3. Visualización de datos
Gráficos de barras:
Comparación de los 20 condados con mayor proporción de vehículos eléctricos.
Evolución de los ratios de adopción de EV por año.
Gráficos de líneas:
Tendencias de adopción de EV segmentadas por uso principal del vehículo (pasajero o camión).
Gráficos de dispersión y pastel:
Relación entre el total de EV y su porcentaje dentro de los condados.
Distribución de tipos de vehículos eléctricos (BEVs y PHEVs).
4. Agrupamiento con K-Means
Análisis de clústeres:
Se agrupan los condados basándose en características como el número total de EV, vehículos híbridos enchufables y porcentaje de EV.
Se utiliza el método del codo (WCSS) y el puntaje de silueta para determinar el número óptimo de clústeres.
5. Conclusiones y patrones observados
Adopción por región y tipo de vehículo:
Algunos condados destacan por tener una mayor proporción de EV, lo que sugiere un mayor avance hacia la electrificación.
Tendencias a lo largo del tiempo:
El número de EV ha incrementado consistentemente, especialmente en vehículos para pasajeros.
Análisis comparativo:
Los BEVs superan a los PHEVs en términos de adopción general.
Segmentación regional:
Los clústeres identificados pueden ayudar a orientar estrategias locales para promover los EV.
Valor del Proyecto
Este análisis proporciona información clave para:
Políticos y urbanistas interesados en fomentar la transición hacia vehículos eléctricos.
Empresas automotrices que buscan identificar mercados prioritarios.
Investigadores interesados en estudiar la evolución del transporte sostenible.

En la limpieza de datos y la creación de columnas temporales de este proyecto se realizaron las siguientes acciones:
1. Limpieza de datos
El objetivo principal fue garantizar que los datos estuvieran en un formato adecuado para análisis y modelado. Esto incluyó:
Conversión de valores a formatos numéricos:
Algunas columnas contenían valores numéricos representados como cadenas, con comas (,) o puntos (.) que debían ser eliminados antes de convertirlos a tipo numérico.
Manejo de datos faltantes:
En caso de que la conversión fallara (debido a valores no válidos), se reemplazaron con NaN utilizando errors='coerce', lo cual permite un manejo controlado de los datos faltantes en análisis posteriores.
2. Creación de columnas temporales
Para facilitar el análisis de tendencias a lo largo del tiempo, se crearon columnas para separar el día, mes y año a partir de la columna de fecha (Date). Esto se logró mediante:
Separación del texto de la fecha:
La fecha en la columna estaba almacenada como texto. Se descompuso en sus partes constituyentes (día, mes, año) utilizando un bucle.
Los valores se almacenaron en listas temporales (days, months, years) y luego se asignaron al DataFrame.
Creación de las nuevas columnas:
Esto permitió que las fechas se analizaran de manera granular (por año, mes o día).
Resultado de estas acciones
Datos limpios y consistentes:
Las columnas clave (Battery Electric Vehicles (BEVs), Total Vehicles, etc.) estaban en formato numérico y listas para análisis.
Análisis temporal habilitado:
Las nuevas columnas (year, month, day) facilitaron análisis detallados, como observar tendencias anuales o mensuales en la adopción de vehículos eléctricos.
Esto fue un paso crucial para garantizar la calidad de los datos y su adecuación a las siguientes fases del proyecto.
