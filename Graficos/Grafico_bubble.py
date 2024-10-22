import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0.0, 0.013030767440795898, 0.05778908729553223, 0.27404093742370605, 0.5691218376159668, 1.005481481552124, 1.5394604206085205, 2.2616047859191895, 3.0742225646972656, 4.001021385192871, 4.877047538757324, 6.893733024597168, 26.292964696884155, 59.40067100524902, 106.49010944366455, 163.20705676078796, 235.02521562576294, 325.60435152053833, 419.4764380455017, 517.734213590622, 688.576504945755]
tiempo_java=[0.000614, 0.001487, 0.010341, 0.018876, 0.022848, 0.038807, 0.061308, 0.107420, 0.127087, 0.167815, 0.214274, 0.262361, 1.149241, 2.692401, 4.970537, 8.215286, 12.566753, 15.763479, 20.940585, 28.969533, 33.281818]
tiempo_cpp=[0, 0.001513, 0.008556, 0.034814, 0.085662, 0.145101, 0.230161, 0.411405, 0.459085, 0.586701, 0.765985, 0.937936, 3.70722, 8.49484, 16.1216, 25.51, 35.0925, 49.9773, 60.92, 76.7151, 96.0973]

# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='green')
plt.plot(tamanos, tiempo_cpp, label='C++', color='pink')
plt.plot(tamanos, tiempo_java, label='Java', color='orange')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de BubbleSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()