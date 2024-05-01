import cv2
import mediapipe as mp
import os

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

# Recognizer class
class Recognizer:
    def __init__(self, templates):
        self.templates = templates

    def recognize(self, points):
        return "Recognition result"

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
        z = landmark.z
        landmarks.append(Point(x, y, z))
    
    return results, landmarks

# Path to dollar.py file
output_file = "dollar.py"

# Initialize MediaPipe Pose model
pose = mp.solutions.pose.Pose()

# Initialize dictionary to store landmarks for each video
video_landmarks = {}

# Get list of video files in the current directory
video_files = [f for f in os.listdir() if f.endswith(".mp4")]

# Loop over each video file in the directory
print("looping over files")
for filename in video_files:
    print(f"looping over file: {filename}")
    video_label = os.path.splitext(filename)[0]
    cap = cv2.VideoCapture(filename)
    landmarks = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        _, frame_landmarks = extract_landmarks(frame, 480, 320)  # Resizing to 480x320
        landmarks.append(frame_landmarks)
    cap.release()
    video_landmarks[video_label] = landmarks

# Function to generate template in dollar.py format
def generate_template(video_label, landmarks):
    template = f"{video_label} = Template('{video_label}', [\n"
    for frame_landmarks in landmarks:
        for landmark in frame_landmarks:
            # Add +10 to each coordinate
            x = landmark.x
            y = landmark.y
            z = 1 #landmark.z
            template += f"Point({x}, {y}, {z}),\n"
    template += "])\n"
    return template

# Generate template for each video
template_code = ""
for video_label, landmarks in video_landmarks.items():
    print(f"Generating template for {video_label}")
    template_code += generate_template(video_label, landmarks)

# Write template code to dollar.py file
# Write template code to dollar.py file
print("Started writing to file")
with open(output_file, "w") as f:
    f.write("from dollarpy import Recognizer, Template, Point\n\n")
    f.write(template_code)
    f.write("\n")  # Add a newline for clarity
    f.write("def trained_model():\n\n")
    # Create the array elements dynamically
    array_elements = ", ".join([f"{video_label}" for video_label in video_landmarks.keys()])

    recognizer1_videos = [f"{video_label}" for video_label in video_landmarks.keys() if not video_label.startswith('n')]
    recognizer2_videos = [f"{video_label}" for video_label in video_landmarks.keys() if video_label.startswith('n')]
    
    f.write(f"  recognizer = Recognizer([{', '.join(recognizer1_videos)}])\n")
    f.write(f"  recognizer2 = Recognizer([{', '.join(recognizer2_videos)}])\n")
        
    i = 0
    list = []
    for video_label in video_landmarks.keys():
        i += 1
        f.write(f"  {video_label}R = Recognizer([{video_label}])\n")
        #list.append({video_label})

    f.write(f"  return recognizer, nrecognizer\n")
        

print("Template generation complete.")

