# Real-Time Face Recognition Attendance System

This project is a Real-Time Face Recognition Attendance System built using OpenCV and face_recognition libraries in Python. The system captures faces from a live webcam feed, recognizes students, and marks their attendance in real-time. The attendance records are stored in a Firebase Realtime Database, and the project also includes integration with Firebase Storage for storing and retrieving student images.

## Features

- **Real-Time Face Detection and Recognition**: Uses OpenCV and face_recognition to detect and recognize faces in real-time.
- **Attendance Logging**: Marks attendance and logs the time for recognized students.
- **Firebase Integration**: 
  - **Realtime Database**: Stores attendance data and student information.
  - **Firebase Storage**: Stores and retrieves student images.
- **Interactive UI**: Displays real-time feed with attendance details and student information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
2. Navigate to the project directory:
   ```bash
   cd face-recognition-attendance
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Set up Firebase:
   - Download your `serviceAccountKey.json` from Firebase and place it in the project root directory.
   - Update the `databaseURL` and `storageBucket` in `main.py` with your Firebase project details.


## Usage

1. Run the project:
   ```bash
   python main.py
2. The webcam will open, and the system will start detecting and recognizing faces in real-time.
3. Attendance will be marked automatically for recognized faces and logged in the Firebase Realtime Database.


## Project Structure

- `main.py`: The main script to run the face recognition and attendance system.
- `Resources/`: Contains images and UI components used in the project.
  - `background.png`: Background image used for the UI.
  - `Modes/`: Contains different mode images used for displaying status in the UI.
- `Encodefile.p`: A serialized file containing the encoded faces and corresponding student IDs.
- `serviceAccountKey.json`: Firebase service account key file (not included in the repository).


## Dependencies

- Python 3.x
- OpenCV
- face_recognition
- cvzone
- numpy
- firebase_admin

  You can install all dependencies using:
  ```bash
  pip install -r requirements.txt
