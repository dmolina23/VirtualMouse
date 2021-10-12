import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

# Variables
wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
cap = cv2.VideoCapture(0)  # 0 is the id of our webcam (i only have one)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.HandDetector(maxHands=1)

while True:
    # 1. Find hand LandMarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

        # 3. Check which fingers are up
        fingers = detector.fingersUp() # See HandTrackingModule.py
        # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
            (255, 0, 255), 2)
    
    # TODO: 4. Only index finger: Moving mode
    # TODO: 5. Convert coordinates
    # TODO: 6. Smoothen values
    # TODO: 7. Move Mouse
    # TODO: 8. Both index and middle fingers: Click mode
    # TODO: 9. Find distance between fingers
    # TODO: 10. Click mouse if distance is short
    
    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
