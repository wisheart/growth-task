import cv2
import mediapipe as mp

video_path = 'C:\\Users\\aishiquan\\Desktop\\tiaowu.mp4'
cap = cv2.VideoCapture(video_path)

output_path = 'C:\\Users\\aishiquan\\Desktop\\tiaowu_after.mp4'
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MP4V'), 30, (frame_width, frame_height))

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_face_detection = mp.solutions.face_detection
hands = mp_hands.Hands()
pose = mp_pose.Pose()
face_detection = mp_face_detection.FaceDetection()

while(True):
    ret, frame = cap.read()
    if ret == True:

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 使用MediaPipe进行人脸检测
        results = face_detection.process(frame_rgb)
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)

    # 使用MediaPipe进行姿势检测
        results = pose.process(frame_rgb)
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 使用MediaPipe进行手势检测
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # 将帧写入输出视频
        output.write(frame)
    else:
        break

    # 显示输出视频
    cv2.namedWindow('Output Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Output Video', 800, 800)  # 设置窗口大小为800x800
    cv2.imshow('Output Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

output.release()