import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

# Variables
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)  # 0 is the id of our webcam (i only have one)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.HandDetector(maxHands=1)

while True:
    # TODO: 1. Find hand LandMarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # TODO: 2. Get the tip of the index and middle fingers
    # TODO: 3. Check which fingers are up
    # TODO: 4. Only index finger: Moving mode
    # TODO: 5. Convert coordinates
    # TODO: 6. Smoothen values
    # TODO: 7. Move Mouse
    # TODO: 8. Both index and middle fingers: Click mode
    # TODO: 9. Find distance between fingers
    # TODO: 10. Click mouse if distance is short
    # TODO: 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
                
    # TODO: 12. Display
