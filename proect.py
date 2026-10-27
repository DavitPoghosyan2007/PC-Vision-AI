
import cv2
import pickle
import numpy as np
import json

# Բեռնում ենք մոդելը
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Դասերի իրական անունները
class_names = ['headset',
 'motherboard',
 'monitor',
 'gpu',
 'microphone',
 'speakers',
 'cpu',
 'mouse',
 'case',
 'cables',
 'hdd',
 'webcam',
 'keyboard',
 'ram']

# Բացում ենք տեսախցիկը
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Տեսախցիկը չի բացվում։")

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Պատկերի նախապատրաստում
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (128, 128))
        img = img.astype("float32") / 255.0
        img = np.expand_dims(img, axis=0)

        # Կանխատեսում
        predictions = model.predict(img, verbose=0)[0]

        class_id = int(np.argmax(predictions))
        confidence = float(predictions[class_id]) * 100

        name = class_names[class_id]

        # Գրում ենք արդյունքը տեսախցիկի վրա
        cv2.putText(
            frame,
            f"{name.upper()} : {confidence:.1f}%",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

        cv2.imshow("PC Parts Recognition", frame)

        # Q՝ դուրս գալու համար
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()

