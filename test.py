import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
# hand object
mp_hands = mp.solutions.hands

# .Hands() has four default parameters
# 1. static_image_mode, it tracks and detects, False means sometime it detects and sometimes it tracks
# 2. max_num_hands
# 3. min_detection_confidence
# 4. min_tracking_confidence

hands = mp_hands.Hands()

while True:
    success, image = cap.read()
    # converting BGR image to RGB
    img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # getting the image
    results = hands.process(img_RGB)
    # showing image
    cv2.imshow("Hand Tracking", image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
