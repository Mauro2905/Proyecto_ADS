import matplotlib.pyplot as plt
import numpy as np

# Tamaños de los datasets (eje X)
tamanos = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
           20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (eje Y) - Datos simulados
tiempo_python = [0.0, 0.006299257278442383, 0.02011895179748535, 0.0882725715637207, 0.19639205932617188, 0.3324546813964844, 0.50872802734375, 0.7294485569000244, 1.0192961692810059, 1.2979536056518555, 1.7405686378479004, 2.135023832321167, 8.87942886352539, 20.82527470588684, 34.285930156707764, 52.088639974594116, 77.92605805397034, 100.23694825172424, 130.10782670974731, 167.37294006347656, 223.42808556556702]
tiempo_java=[0.000190, 0.000959, 0.002275, 0.005412, 0.009828, 0.016572, 0.020993, 0.024220, 0.027135, 0.041530, 0.051515, 0.156866, 0.243524, 0.544035, 1.148699, 1.543029, 2.213675, 2.896782, 4.017274, 5.036221, 6.024791]
tiempo_cpp=[0, 0.001, 0.001999, 0.009539, 0.022395, 0.042129, 0.061863, 0.093829, 0.126821, 0.155823, 0.195094, 0.266883, 1.07481, 2.3155, 4.19092, 6.36697, 9.10698, 12.428, 16.3354, 20.7389, 25.6006]



# Crear la figura y la gráfica
plt.plot(tamanos, tiempo_python, label='Python', color='green')
plt.plot(tamanos, tiempo_cpp, label='C++', color='pink')
plt.plot(tamanos, tiempo_java, label='Java', color='orange')
# Configuración de la gráfica
plt.xlabel('Tamaño del Dataset')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de SeleccionSort en Python - C++ - Java')
plt.legend()

# Rotar las etiquetas del eje X para mejor visibilidad
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()