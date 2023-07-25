import cv2
import mediapipe as mp

# 初始化MediaPipe Face Mesh
mp_drawing = mp.solutions.drawing_utils  #绘图方法
mp_drawing_styles = mp.solutions.drawing_styles  #绘图样式
mp_face_mesh = mp.solutions.face_mesh  # mediapipe 人脸网格方法
drawing_spec = mp_drawing.DrawingSpec(thickness=0.5, circle_radius=0.5)  #绘图参数设定

# hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
#风格设计
mpDraw = mp.solutions.drawing_utils
handLmsStyle = mpDraw.DrawingSpec(color=(0,0,0), thickness=2)#点
handConStyle = mpDraw.DrawingSpec(color=(255,255,255), thickness=2)#线

# Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
#风格设计
mpDraw = mp.solutions.drawing_utils
poseLmsStyle = mpDraw.DrawingSpec(color=(0, 255, 255), thickness=4)  #点
poseConStyle = mpDraw.DrawingSpec(color=(255, 0, 255), thickness=2)  #线
# 加载视频或摄像头
cap = cv2.VideoCapture("C:/Users/33853/Desktop/xh.mp4")  # 使用摄像头，如果要从视频文件中读取，请替换参数为视频文件路径
#cap = cv2.VideoCapture(0)



# 获取原始帧大小
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 减小帧大小
new_width = int(width* 2)
new_height = int(height *2)

# face
# 啟用人臉網格偵測，設定相關參數
with mp_face_mesh.FaceMesh(
        max_num_faces=1,  # 一次偵測最多幾個人臉
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    # hands
    with mpHands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

        # pose
        with mp_pose.Pose(
                static_image_mode=False, min_detection_confidence=0.5) as pose:

            while cap.isOpened():
                # 读取视频帧
                ret, frame = cap.read()
                if not ret:
                    break

                # 调整帧的大小
                frame = cv2.resize(frame, (new_width, new_height))

                # 转换帧为RGB格式
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # 进行人脸网格检测
                face_results = face_mesh.process(image_rgb)

                # 绘制面部结果
                if face_results.multi_face_landmarks:
                    for face_landmarks in face_results.multi_face_landmarks:
                        # 繪製網格
                        mp_drawing.draw_landmarks(
                            image=frame,
                            landmark_list=face_landmarks,
                            connections=mp_face_mesh.FACEMESH_TESSELATION,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_tesselation_style())
                        # 繪製輪廓
                        mp_drawing.draw_landmarks(
                            image=frame,
                            landmark_list=face_landmarks,
                            connections=mp_face_mesh.FACEMESH_CONTOURS,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_contours_style())
                        # 繪製眼睛
                        mp_drawing.draw_landmarks(
                            image=frame,
                            landmark_list=face_landmarks,
                            connections=mp_face_mesh.FACEMESH_IRISES,
                            landmark_drawing_spec=None,
                            connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_iris_connections_style())

                # 进行手部检测
                hands_results = hands.process(image_rgb)
                # 绘制手部结果
                if hands_results.multi_hand_landmarks:
                    for handLms in hands_results.multi_hand_landmarks:
                        mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)

                # 进行姿态检测
                pose_results = pose.process(image_rgb)

                # 绘制姿态结果
                if pose_results.pose_landmarks:
                    mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=pose_results.pose_landmarks,
                        connections=mp_pose.POSE_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
                        connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2),
                    )

                # 显示结果
                cv2.imshow('studio', frame)
                if cv2.waitKey(5) == ord('q'):
                    break