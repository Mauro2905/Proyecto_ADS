import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0.0, 0.0010001659393310547, 0.0011074542999267578, 0.0019953250885009766, 0.004126071929931641, 0.004537820816040039, 0.00656437873840332, 0.0075109004974365234, 0.007518291473388672, 0.0075299739837646484, 0.007561206817626953, 0.009022951126098633, 0.021242618560791016, 0.03147411346435547, 0.04432821273803711, 0.055665016174316406, 0.06261539459228516, 0.06990909576416016, 0.07126855850219727, 0.08562707901000977, 0.15880274772644043]
tiempo_java=[0.000100, 0.000507, 0.000521, 0.000560, 0.000601, 0.000721, 0.000796, 0.000910, 0.001001, 0.001247, 0.002045, 0.002331, 0.004250, 0.006773, 0.007131, 0.007242, 0.008816, 0.009954, 0.010176, 0.011874, 0.024428]
tiempo_cpp=[0, 0, 0.001031, 0, 0.001001, 0, 0.001, 0.000509, 0.000507, 0.001002, 0.001, 0.001998, 0.00449, 0.009509, 0.009543, 0.01203, 0.016026, 0.020106, 0.025086, 0.031988, 0.030874]



# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='green')
plt.plot(tamanos, tiempo_cpp, label='C++', color='pink')
plt.plot(tamanos, tiempo_java, label='Java', color='orange')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de QuickSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()