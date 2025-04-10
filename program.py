import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
TF_ENABLE_ONEDNN_OPTS=0

def create_model():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train / 255.0
    X_test = X_test / 255.0

    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=1)
    return model


model = create_model() #-------------------->una vez creado el .h5 comentar esta linea
model.save('mnist_model.h5')
#model = load_model('mnist_model.h5') #-----> una vez creado el .h5 descomentar esta linea


window = np.ones((280, 280), dtype=np.uint8) * 255
drawing = False

def draw(event, x, y, flags, param):
    global drawing, window
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(window, (x, y), 10, (0, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("Dibuja un número")
cv2.setMouseCallback("Dibuja un número", draw)


def predict_digit(img):
    img = cv2.resize(img, (28, 28))
    img = cv2.bitwise_not(img)
    img = img.reshape(1, 28, 28, 1)
    img = img / 255.0
    prediction = model.predict(img)
    return np.argmax(prediction), np.max(prediction)


feedback = {"correct": 0, "incorrect": 0}

while True:
    cv2.imshow("Dibuja un número", window)
    key = cv2.waitKey(1) & 0xFF


    if key == ord('c'):
        digit, confidence = predict_digit(window)
        print(f"¡Creo que es un {digit}! (Confianza: {confidence:.2f})")


        user_feedback = input("¿Fue correcto? (s/n): ").lower()
        if user_feedback == 's':
            feedback["correct"] += 1
            print("¡Gracias por tu feedback! 👍")
        else:
            feedback["incorrect"] += 1
            print("¡Intentaré mejorar! 👎")


        window = np.ones((280, 280), dtype=np.uint8) * 255


    elif key == ord('q'):
        print(f"\nResumen de Feedback:")
        print(f"✅ Correctas: {feedback['correct']}")
        print(f"❌ Incorrectas: {feedback['incorrect']}")
        break

cv2.destroyAllWindows()