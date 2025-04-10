# NUMBERS
### Introduction:
This program is an interactive tool that uses Machine Learning to recognize handwritten digits.

### How does it work?
Draw: Use the mouse to write a number (0-9) in the black window.

Predict: Press the c key so that the model will predict the drawn number.

Feedback: Confirms if the prediction was correct (s = yes, n = no), helping to improve the system.

### Key technologies:
TensorFlow/Keras: Convolutional neural network (CNN) model trained with the MNIST dataset.

OpenCV: Real-time drawing interface.

Feedback system: records model accuracy for future improvements.

### Requirements:
Requires opencv-python and tensorflow.

It can be installed by running the following command:

<code>pip install opencv-python tensorflow numpy.</code>

### Instructions:
First run: Will automatically train the model (takes ~1 minute).

Subsequent runs: Will load the saved model (instantaneous).

### Controls:
Draw with the mouse.

Press <code>C</code> to predict.

Press <code>Q</code> to exit.

# Captures

### No Drawing
<img src ="/img/sin dibujo.png">

### Drawing
<img src ="/img/dibujo.png">

### Result
<img src ="/img/s o n.png">

### Positive
<img src ="/img/s.png">

### Negative
<img src ="/img/n.png">
