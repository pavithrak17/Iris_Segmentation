# Import required libraries
from operator import rshift
import cv2 as cv 
import numpy as np
import mediapipe as mp 

# Initialize Mediapipe's face mesh solution
mp_face_mesh = mp.solutions.face_mesh

# Indices for landmarks representing left and right eyes and irises
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

# Start video capture
cap = cv.VideoCapture(0)

# Initialize face mesh detector with parameters
with mp_face_mesh.FaceMesh(
    max_num_faces=1,                   # Track only one face
    refine_landmarks=True,              # Refine landmark positions around eyes
    min_detection_confidence=0.5,       # Confidence threshold for detecting face
    min_tracking_confidence=0.5         # Confidence threshold for tracking face landmarks
) as face_mesh:
    # Loop for reading frames from the webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Exit loop if frame not read successfully

        # Flip the frame horizontally for a mirror effect
        frame = cv.flip(frame, 1)

        # Convert the frame color to RGB for Mediapipe processing
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        # Get the height and width of the image for scaling
        img_h, img_w = frame.shape[:2]

        # Process the frame and detect face landmarks
        results = face_mesh.process(rgb_frame)

        # Check if landmarks are detected
        if results.multi_face_landmarks:
            # Convert landmark points into an array of pixel coordinates
            mesh_points = np.array([
                np.multiply([p.x, p.y], [img_w, img_h]).astype(int) 
                for p in results.multi_face_landmarks[0].landmark
            ])

            # Calculate the enclosing circle for left and right irises
            (l_cx, l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
            (r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
            
            # Center coordinates of left and right iris
            center_left = np.array([l_cx, l_cy], dtype=np.int32)
            center_right = np.array([r_cx, r_cy], dtype=np.int32)
            
            # Draw circles around the left and right irises
            cv.circle(frame, center_left, int(l_radius), (255, 0, 255), 1, cv.LINE_AA)
            cv.circle(frame, center_right, int(r_radius), (255, 0, 255), 1, cv.LINE_AA)
        
        # Display the frame with drawn annotations
        cv.imshow('img', frame)

        # Exit loop if 'q' key is pressed
        key = cv.waitKey(1)
        if key == ord('q'):
            break

# Release the video capture and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
