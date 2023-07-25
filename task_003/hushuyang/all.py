import cv2
import mediapipe as mp

# Create a VideoCapture object to read the input video
cap = cv2.VideoCapture("D:\CNTV\Download\dance.mp4")

# Create a VideoWriter object to save the output video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('combined_detection.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# MediaPipe hands detection
mp_hands = mp.solutions.hands.Hands(static_image_mode=False,
                                    max_num_hands=2,
                                    min_detection_confidence=0.5,
                                    min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# MediaPipe pose detection
mp_pose = mp.solutions.pose.Pose()
mp_pose_drawing = mp.solutions.drawing_utils

# OpenCV face and eye detection
face_cascade = cv2.CascadeClassifier("D://BaiduNetdiskDownload//xml//haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("D://BaiduNetdiskDownload//xml//haarcascade_eye.xml")

# Loop through the input video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Clone the frame for displaying all the detection results
    display_frame = frame.copy()

    # Detect hands using MediaPipe
    hands_results = mp_hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if hands_results.multi_hand_landmarks:
        for hand_landmarks in hands_results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(display_frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    # Detect pose using MediaPipe
    pose_results = mp_pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if pose_results.pose_landmarks:
        mp_pose_drawing.draw_landmarks(display_frame, pose_results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)

    # Detect faces and eyes using OpenCV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(display_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = display_frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the combined detection results in a single window
    cv2.imshow('Combined Detection', display_frame)

    # Write the current frame to the output video file
    out.write(display_frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
