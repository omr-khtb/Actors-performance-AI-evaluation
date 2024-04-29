import cv2
import mediapipe as mp
from dollarpy import Recognizer, Template, Point
# Point class
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Template class
class Template:
    def __init__(self, name, points):
        self.name = name
        self.points = points

# Function to extract landmarks from a frame using MediaPipe
def extract_landmarks(frame, target_width, target_height):
    # Resize the frame
    resized_frame = cv2.resize(frame, (target_width, target_height))
    
    # Convert the frame to RGB format
    RGB = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    
    # Process the RGB frame to get the result
    results = pose.process(RGB)
    
    landmarks = []
    for landmark in results.pose_landmarks.landmark:
        # Scale the landmarks according to the resized frame
        x = landmark.x * target_width
        y = landmark.y * target_height
        z = 1  # Set z-coordinate to 1
        landmarks.append(Point(x, y, z))
    
    return landmarks

# Initialize MediaPipe Pose model
pose = mp.solutions.pose.Pose()

# Initialize dictionary to store landmarks for each video
video_landmarks = {}

# Get list of video files in the current directory
video_files = ["test.mp4"]  # Add your video file(s) here

# Loop over each video file in the directory
for filename in video_files:
    cap = cv2.VideoCapture(filename)
    landmarks = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_landmarks = extract_landmarks(frame, 480, 320)  # Resizing to 480x320
        landmarks.append(frame_landmarks)
    cap.release()
    video_landmarks[filename] = landmarks

# Generate template for each video
template_dict = {}
for video_file, landmarks in video_landmarks.items():
    template_points = []
    for frame_landmarks in landmarks:
        for landmark in frame_landmarks:
            # Add landmarks to template with z-coordinate fixed at 1
            x = landmark.x
            y = landmark.y
            z = 1
            template_points.append(Point(x, y, z))
    template_dict[video_file] = Template(video_file, template_points)

# Example of how to access template points

temp = []
for video_file, template in template_dict.items():
    points_array = []
    for point in template.points:
        points_array.append(Point(point.x, point.y, point.z))
    temp.append((video_file, points_array))

with open("dollar.py", 'r') as source:
         content = source.readlines()

with open("final.py", "w") as output_file:
    output_file.writelines(content)
    output_file.write("result = recognizer.recognize([\n")
    for point in template.points:
        output_file.write(f"Point({point.x},{point.y},{point.z}),\n")
    output_file.write("])\n")
    output_file.write("print(result)\n")
    j = 0
    for i in range (7):
        j+=1
        output_file.write(f"result{j} = recognizer{j}.recognize([\n")
        for point in template.points:
            output_file.write(f"Point({point.x},{point.y},{point.z}),\n")
        output_file.write("])\n")
        print(i)
        output_file.write(f"print(result{j})\n")
    






