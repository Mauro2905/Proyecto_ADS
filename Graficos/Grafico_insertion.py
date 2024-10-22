import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0.0, 0.0050008296966552734, 0.019603967666625977, 0.09328293800354004, 0.19173550605773926, 0.3549327850341797, 0.5099155902862549, 0.7308743000030518, 0.9904022216796875, 1.3456645011901855, 1.5868148803710938, 2.138415575027466, 8.948569059371948, 20.209150791168213, 36.30526661872864, 53.97874641418457, 84.03012990951538, 108.74827194213867, 125.54564213752747, 166.34351348876953, 231.74601459503174]
tiempo_java=[0.000172, 0.000474, 0.002524, 0.005997, 0.010380, 0.013757, 0.023983, 0.027588, 0.036449, 0.040889, 0.060012, 0.097343, 0.278501, 0.640083, 1.170131, 1.729506, 2.546878, 3.456557, 4.632243, 6.005115, 7.085436]
tiempo_cpp=[0, 0.001398, 0.002018, 0.007472, 0.016535, 0.028374, 0.044641, 0.068597, 0.086644, 0.116724, 0.157798, 0.191485, 0.741606, 1.66075, 3.04814, 4.6423, 6.80772, 9.79871, 11.964, 15.2601, 19.5074]



# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='green')
plt.plot(tamanos, tiempo_cpp, label='C++', color='pink')
plt.plot(tamanos, tiempo_java, label='Java', color='orange')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de InsertionSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()