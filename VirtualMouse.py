import cv2
import numpy as np
import HandTrackingModule1 as htm
import time
import autopy

# Constants
wCam, hCam = 640, 480  # Camera resolution
frameR = 100  # Frame reduction for smoother movement
smoothening = 7  # Smoothening factor

# Previous and current locations for cursor movement
pLocX, pLocY = 0, 0
cLocX, cLocY = 0, 0

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Initialize hand detector
handDetector = htm.handDetector(maxHands=1)

# Get screen size
wScr, hScr = autopy.screen.size()

# Main loop
while True:
    # Capture frame and detect hands
    success, img = cap.read()
    img = handDetector.findHands(img)
    lmList, bbox = handDetector.findPosition(img)

    if lmList:
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip
        
        # Check which fingers are up
        fingers = handDetector.fingersUp()
        
        # Draw movement boundary
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        
        # Moving mode (Only index finger up)
        if fingers[1] and not fingers[2]:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            
            # Smoothen values
            cLocX = pLocX + (x3 - pLocX) / smoothening
            cLocY = pLocY + (y3 - pLocY) / smoothening
            
            # Move mouse
            autopy.mouse.move(wScr - cLocX, cLocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            
            pLocX, pLocY = cLocX, cLocY
        
        # Clicking mode (Index and middle fingers up)
        if fingers[1] and fingers[2]:
            length, img, lineInfo = handDetector.findDistance(8, 12, img)
            
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
    
    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if 'pTime' in locals() else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    # Display output
    cv2.imshow("Video", img)
    cv2.waitKey(1)
