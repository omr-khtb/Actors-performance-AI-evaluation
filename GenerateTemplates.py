import os
import cv2
import mediapipe as mp

# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

def extract_landmarks(frame):
    # convert the frame to RGB format
    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # process the RGB frame to get the result
    results = pose.process(RGB)
    
    landmarks = []
    for landmark in results.pose_landmarks.landmark:
        landmarks.append((landmark.x, landmark.y, landmark.z))
    
    return results, landmarks

def StartTest(directory):
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)) and file_name.endswith(".mp4"):
            print("Processing:", file_name)
            
            cap = cv2.VideoCapture(os.path.join(directory, file_name))
            framecnt = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                
                # Resize frame
                frame = cv2.resize(frame, (480, 320))
                
                results, landmarks = extract_landmarks(frame)
                print("Frame:", framecnt)
                print("Landmarks:", landmarks)
                
                framecnt += 1
                
                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                cv2.imshow('Output', frame)
                
                if cv2.waitKey(1) == ord('q'):
                    break
            
            cap.release()
            cv2.destroyAllWindows()

# Example usage
directory_path1 = "F:\My projects\Actors Research project\Actors-performance-AI-evaluation"
StartTest(directory_path1)
