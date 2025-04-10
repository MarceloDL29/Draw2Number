# NUMBERS
### Introducción:
Este programa es una herramienta interactiva que utiliza Machine Learning para reconocer dígitos escritos a mano.

### ¿Como funciona?

Dibuja: Usa el mouse para escribir un número (0-9) en la ventana negra.

Predice: Presiona la tecla c para que el modelo predecirá el número dibujado.

Feedback: Confirma si la predicción fue correcta (s = sí, n = no), ayudando a mejorar el sistema.

### Tecnologías clave:

TensorFlow/Keras: Modelo de red neuronal convolucional (CNN) entrenado con el dataset MNIST.

OpenCV: Interfaz de dibujo en tiempo real.

Sistema de feedback: Registra la precisión del modelo para futuras mejoras.

### Requisitos:

Requiere opencv-python y tensorflow.

Se puede instalar ejecutando el siguiente comando:

<code>pip install opencv-python tensorflow numpy</code>

### Instrucciones:

Primera ejecución: Entrenará automáticamente el modelo (tarda ~1 minuto).

Ejecuciones posteriores: Cargará el modelo guardado (instantáneo).

### Controles:

Dibuja con el mouse.

Presiona <code>C</code> para predecir.

Presiona <code>Q</code> para salir.

<img src ="../img/s">

