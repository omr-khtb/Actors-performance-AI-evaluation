import cv2
import mediapipe as mp

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# Initialize MediaPipe Pose model
pose = mp.solutions.pose.Pose()

# Define sliding window parameters
window_size = 48  # Number of frames to accumulate before recognition
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

ctgwa = 0
# Open video capture object
cap = cv2.VideoCapture("hands_chest_frown.mp4")
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total frames:", total_frames)

CurrentFrame = 0
while cap.isOpened():

    CurrentFrame +=1

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
        if window_size + CurrentFrame > total_frames -1:
           print("left current fram: ",CurrentFrame )
           if total_frames == CurrentFrame -1 :
             landmarks_buffer.append(frame_buffer)
             print("appended last")
        elif len(frame_buffer) >= window_size:
                ctgwa += 1
                print("countgwa: ",ctgwa)
                print("this is frame_ buffer" , len(frame_buffer))
                print("this is current frames" , CurrentFrame)
                print("\n")
                # Add landmarks of the current window to the landmarks buffer
                landmarks_buffer.append(frame_buffer)
                
                # Pop out a number of frames from the beginning to overlap
                frame_buffer = frame_buffer[window_size-overlap_frames:]

        
    except Exception as e:
        print('Error:', e)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

print("this is count gwa" , ctgwa)
# Release video capture object
cap.release()
cv2.destroyAllWindows()
# Loop through landmarks_buffer and print out each list of landmarks
#list = []
#for window_landmarks in landmarks_buffer:
    #print("Window Landmarks:")
    #for landmarks in window_landmarks:
        #list.append([Point(point.x, point.y, 1) for point in landmarks])
    #print("End of Window\n")

# Now, landmarks_buffer contains lists of landmarks for each sliding window

ct = 0
for window_landmarks in landmarks_buffer:
    #print("Window Landmarks:")
    ct += 1

    #for landmarks in window_landmarks:
        #print([(point.x, point.y, 1) for point in landmarks])
        
    #print("End of Window\n")
print("this is number of seg: " , ct)
    
i = 0
with open("final.py", "w") as output_file:
    output_file.write("exec(open('dollar.py').read())\n")
    output_file.write("recognizer = trained_model()\n")
    output_file.write("listp = []\n")
    output_file.write("listn = []\n")
    output_file.write("listpr = []\n")
    output_file.write("listnr = []\n")
    output_file.write("listfinal = []\n")
    for window_landmarks in landmarks_buffer:
        i += 1
        output_file.write(f"result{i} = recognizer[0].recognize([\n")
        for landmarks in window_landmarks:
            for point in landmarks:
                output_file.write(f"Point({point.x},{point.y},1),\n")
        output_file.write("])\n")
        

        output_file.write(f"listpr.append(result{i})\n")

        output_file.write("flag = 0\n")
        output_file.write("for item in listp:\n")
        output_file.write(f"  if item[0]== result{i}[0]:\n")
        output_file.write("      flag = 1\n")
        output_file.write("if flag == 0 :\n")
        output_file.write(f"  listp.append(result{i})\n")

    i = 0
    for window_landmarks in landmarks_buffer:
          i += 1
          output_file.write(f"resultn{i} = recognizer[1].recognize([\n")
          for landmarks in window_landmarks:
            for point in landmarks:
                output_file.write(f"Point({point.x},{point.y},1),\n")
          output_file.write("])\n")
          output_file.write(f"listnr.append(resultn{i})\n")
        
          output_file.write("flag = 0\n")
          output_file.write("for item in listn:\n")
          output_file.write(f"  if item[0]== resultn{i}[0]:\n")
          output_file.write("      flag = 1\n")
          output_file.write("if flag ==0 :\n")
          output_file.write(f"  listn.append(resultn{i})\n")
          

          output_file.write(f"if result{i}[0]== 'n' + resultn{i}[0]:\n")
          output_file.write(f"  if result{i}[1] >=  resultn{i}[1]:\n")
          output_file.write(f"      fonallist.append(result{i})\n")
          output_file.write(f"  else:\n")
          output_file.write(f"     fonallist.append(resultn{i})\n")
    i = 0
    for window_landmarks in landmarks_buffer:
          i += 1
          output_file.write(f"print('this is each frame result with postive recognizer:')\n")
          output_file.write(f"print(result{i})\n\n")
          output_file.write(f"print('this is each frame result with negative recognizer:')\n")
          output_file.write(f"print(resultn{i})\n\n")

         #output_file.write(f"print('this is list of actions with postive list repeated:')\n")
         #output_file.write(f"for item in listp\n")
         #output_file.write(f"  print(item)\n")

          output_file.write(f"print('this is list of actions with postive list unrepeated:')\n")
          output_file.write(f"print(listp)\n\n")

          output_file.write(f"print('this is list of actions with postive list repeated:')\n")
          output_file.write(f"print(listpr)\n\n")

          output_file.write(f"print('this is list of actions with negative list unrepeated:')\n")
          output_file.write(f"print(listn)\n\n")

          output_file.write(f"print('this is list of actions with negative list repeated:')\n")
          output_file.write(f"print(listnr)\n\n")

          output_file.write(f"print('this is final list of actions')\n")
          output_file.write(f"print(listfinal)\n\n")


          output_file.write(f"print('this is accuracy number of moves of total number of moves')\n")
          output_file.write(f"print(len(listfinal)/recognizer[3])\n\n")
    



        
    
    
    
    #j = 0
    #for i in range (7):
    #    j+=1
     #   output_file.write(f"result{j} = recognizer{j}.recognize([\n")
      #  for point in list.points:
       #     output_file.write(f"Point({point.x},{point.y},{point.z}),\n")
        #output_file.write("])\n")
        
        #print(i)
        #output_file.write(f"print(result{j})\n")
