Virtual Mouse with Hand Tracking
This project implements a virtual mouse using hand tracking with OpenCV, MediaPipe, and AutoPy. The application uses a webcam to detect hand movements and gives users the ability to move the cursor and click with gestures.
# Reqirements
Make sure Python is installed on your computer, then use the following command to install the necessary dependencies:
pip Install the media pipe for opencv-python numpy autopy.
Setting up and carrying out
1. Download the script or clone this repository.
2. In the same directory, make sure the HandTrackingModule2.py file is located.
3. Use Python script.py to launch the script.
# Module for Hand Tracking
The hand tracking mechanism is contained in the HandTrackingModule1.py file. Among its features are landmark tracking and hand detection.
1. Identification of finger position.
2. Recognizing gestures, such as counting fingers and calculating distance.
# Usage of this Project
1. Move Cursor: To move the mouse cursor, raise only the index finger.
2. Click: To mimic a mouse click, raise your index and middle fingers and then bring them close together.
3. Exit: Either close the OpenCV window or press Esc.
# Troubleshooting
1. Make sure your webcam is connected and reachable if it doesn't initialize.
2. Use pip install -r requirements.txt to install dependencies if any are missing.
3. For improved control, modify the smoothening and frameR settings.
# Authorization
1.This project can be altered as needed because it is open-source.
2. Consider including gesture-based right-click functionality or scroll motions for even more improvements.

