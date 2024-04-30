import cv2
import mediapipe as mp
from Dollar import recognizer1, Point

# Initialize MediaPipe Pose model
pose = mp.solutions.pose.Pose()

# Define sliding window parameters
window_size = 23  # Number of frames to accumulate before recognition
overlap_frames = 5  # Number of frames to overlap between consecutive windows

# Initialize variables
frame_buffer = []  # Buffer to store frames
landmarks_buffer = []  # Buffer to store landmarks of each sliding window

# Function to extract landmarks from a frame
def extract_landmarks(frame):
    # Convert the frame to RGB format
    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the RGB frame to get the result
    results = pose.process(RGB)
    
    landmarks = []
    for landmark in results.pose_landmarks.landmark:
        # Scale the landmarks according to the frame size
        x = landmark.x * frame.shape[1]
        y = landmark.y * frame.shape[0]
        z = 1  # Set z-coordinate to 1
        landmarks.append(Point(x, y, z))
    
    return landmarks

# Open video capture object
cap = cv2.VideoCapture("hands_chest_frown.mp4")

while cap.isOpened():
    # Read frame from capture object
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Resize frame to a specific size (optional)
    frame = cv2.resize(frame, (480, 320))
    
    try:
        # Extract landmarks from the frame
        frame_landmarks = extract_landmarks(frame)
        
        # Append landmarks to frame buffer
        frame_buffer.append(frame_landmarks)
        
        # Check if enough frames are accumulated for recognition
        if len(frame_buffer) >= window_size:
            # Add landmarks of the current window to the landmarks buffer
            landmarks_buffer.append(frame_buffer)
            
            # Pop out a number of frames from the beginning to overlap
            frame_buffer = frame_buffer[overlap_frames:]
        
    except Exception as e:
        print('Error:', e)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture object
cap.release()
cv2.destroyAllWindows()
# Loop through landmarks_buffer and print out each list of landmarks
for window_landmarks in landmarks_buffer:
    print("Window Landmarks:")
    for landmarks in window_landmarks:
        print([(point.x, point.y, 1) for point in landmarks])
    print("End of Window\n")

# Now, landmarks_buffer contains lists of landmarks for each sliding window
