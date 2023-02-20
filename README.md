# Facial-Recognition-Using-Python-OpenCV
This is a project that uses Python and OpenCV to perform facial detection and recognition. The project includes a script that captures video from a webcam, detects faces in each frame, and recognizes them if they are already known to the system.

Installation

To run this project, you will need to install the following dependencies:

    Python 3.6 or higher
    OpenCV 4.5.3 or higher
    NumPy
    Pillow
    dlib
    face_recognition

You can install these dependencies using pip by running the following command:
pip install opencv-python numpy Pillow dlib face_recognition

Usage

To use this project, run the facial_recognition.py script. The script will capture video from your default webcam and display the output with facial detection and recognition overlays.

To add new faces to the system, create a folder with the person's name in the known_faces directory and add one or more images of their face to the folder. The script will automatically detect and recognize new faces in subsequent video frames.
Credits

This project uses the face_recognition library, which is built on top of dlib and OpenCV.
