import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0.0, 0.0010030269622802734, 0.001996278762817383, 0.006774187088012695, 0.007803916931152344, 0.010524988174438477, 0.015529870986938477, 0.016521215438842773, 0.020087242126464844, 0.027026653289794922, 0.03007340431213379, 0.03365588188171387, 0.08090877532958984, 0.12082314491271973, 0.15230178833007812, 0.18460512161254883, 0.2618260383605957, 0.2758820056915283, 0.29185914993286133, 0.333876371383667, 0.3925487995147705]
tiempo_java=[0.000082, 0.000526, 0.000534, 0.000721, 0.000754, 0.000891, 0.001178, 0.001236, 0.001533, 0.001852, 0.003893, 0.003918, 0.008000, 0.009815, 0.010437, 0.011562, 0.011917, 0.016893, 0.020349, 0.021810, 0.023953]
tiempo_cpp=[0, 0, 0, 0.001007, 0.001, 0.003002, 0.003, 0.004, 0.005001, 0.004675, 0.005999, 0.006525, 0.013034, 0.021805, 0.026168, 0.032597, 0.042668, 0.049928, 0.060739, 0.065822, 0.073684]



# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='green')
plt.plot(tamanos, tiempo_cpp, label='C++', color='pink')
plt.plot(tamanos, tiempo_java, label='Java', color='orange')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de MergeSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()