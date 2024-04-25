import os
import cv2
import mediapipe as mp
# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
framecnt=0


from dollarpy import Recognizer, Template, Point
Drink = Template('Drink', [
Point(65,463, 1),
Point(430,363, 1),
Point(61,471, 1),
Point(446,361, 1),
Point(57,476, 1),
Point(454,356, 1),
Point(54,477, 1),
Point(479,339, 1),
Point(52,477, 1),
Point(489,316, 1),
Point(41,477, 1),
Point(506,304, 1),
Point(23,476, 1),
Point(510,302, 1),
Point(25,476, 1),
Point(508,307, 1),
Point(43,477, 1),
Point(506,304, 1),
Point(48,485, 1),
Point(501,282, 1),
Point(48,488, 1),
Point(454,251, 1),
Point(49,490, 1),
Point(404,218, 1),
Point(50,489, 1),
Point(358,194, 1),
Point(56,496, 1),
Point(333,181, 1),
Point(58,496, 1),
Point(321,174, 1),
Point(57,495, 1),
Point(313,170, 1),
Point(54,494, 1),
Point(313,168, 1),
Point(52,490, 1),
Point(314,165, 1),
Point(50,486, 1),
Point(309,153, 1),
Point(49,485, 1),
Point(309,147, 1),
Point(49,484, 1),
Point(305,130, 1),
Point(49,484, 1),
Point(302,118, 1),
Point(41,484, 1),
Point(296,110, 1),
Point(42,483, 1),
Point(298,108, 1),
Point(38,485, 1),
Point(298,105, 1),
Point(37,487, 1),
Point(294,101, 1),
Point(36,487, 1),
Point(294,100, 1),
Point(33,480, 1),
Point(293,104, 1),
Point(34,479, 1),
Point(296,114, 1),
Point(39,482, 1),
Point(297,151, 1),
Point(38,482, 1),
Point(324,216, 1),
Point(47,482, 1),
Point(330,266, 1),
Point(50,486, 1),
Point(377,333, 1),
Point(49,486, 1),
Point(396,353, 1),
Point(49,485, 1),
Point(415,359, 1),
Point(48,483, 1),
Point(413,354, 1),
Point(43,479, 1),
Point(412,354, 1),
Point(48,478, 1),
Point(412,354, 1),
Point(65,480, 1),
Point(411,350, 1),
])
Harsh = Template('Harsh', [
Point(62,461, 1),
Point(323,218, 1),
Point(53,457, 1),
Point(304,203, 1),
Point(52,459, 1),
Point(304,197, 1),
Point(51,461, 1),
Point(300,193, 1),
Point(46,463, 1),
Point(303,192, 1),
Point(42,463, 1),
Point(303,191, 1),
Point(41,463, 1),
Point(302,193, 1),
Point(38,463, 1),
Point(308,191, 1),
Point(17,463, 1),
Point(309,150, 1),
Point(16,469, 1),
Point(294,102, 1),
Point(5,469, 1),
Point(283,89, 1),
Point(2,467, 1),
Point(274,77, 1),
Point(7,475, 1),
Point(270,73, 1),
Point(15,475, 1),
Point(272,78, 1),
Point(25,474, 1),
Point(276,78, 1),
Point(28,474, 1),
Point(274,73, 1),
Point(29,473, 1),
Point(275,76, 1),
Point(29,472, 1),
Point(276,80, 1),
Point(34,472, 1),
Point(276,77, 1),
Point(43,473, 1),
Point(276,74, 1),
Point(38,473, 1),
Point(277,79, 1),
Point(38,472, 1),
Point(277,81, 1),
Point(40,472, 1),
Point(276,78, 1),
Point(40,468, 1),
Point(276,79, 1),
Point(39,468, 1),
Point(281,80, 1),
])
HarshLeft = Template('HarshLeft', [
Point(40,472, 1),
Point(418,418, 1),
Point(50,471, 1),
Point(427,427, 1),
Point(50,469, 1),
Point(423,422, 1),
Point(76,475, 1),
Point(428,434, 1),
Point(58,497, 1),
Point(418,451, 1),
Point(127,111, 1),
Point(419,430, 1),
Point(160,53, 1),
Point(417,415, 1),
Point(168,39, 1),
Point(419,425, 1),
Point(171,36, 1),
Point(418,419, 1),
Point(168,39, 1),
Point(420,416, 1),
Point(172,39, 1),
Point(423,406, 1),
Point(168,39, 1),
Point(421,409, 1),
Point(170,40, 1),
Point(419,406, 1),
Point(171,39, 1),
Point(417,396, 1),
Point(171,41, 1),
Point(419,390, 1),
Point(170,41, 1),
Point(420,385, 1),
Point(168,50, 1),
Point(420,399, 1),
Point(105,479, 1),
Point(432,395, 1),
Point(80,486, 1),
Point(435,395, 1),
Point(65,481, 1),
Point(436,393, 1),
Point(71,484, 1),
Point(438,393, 1),
Point(60,487, 1),
Point(438,392, 1),
Point(58,491, 1),
Point(437,406, 1),
Point(53,491, 1),
Point(437,410, 1),
Point(56,495, 1),
Point(440,403, 1),
])
Drinkingmobile = Template('Drinkingmobile', [
Point(107,473, 1),
Point(426,450, 1),
Point(116,469, 1),
Point(425,449, 1),
Point(119,458, 1),
Point(409,442, 1),
Point(115,465, 1),
Point(408,441, 1),
Point(113,461, 1),
Point(408,441, 1),
Point(111,458, 1),
Point(409,450, 1),
Point(155,420, 1),
Point(408,445, 1),
Point(174,394, 1),
Point(409,443, 1),
Point(170,393, 1),
Point(408,443, 1),
Point(173,396, 1),
Point(409,445, 1),
Point(173,396, 1),
Point(404,444, 1),
Point(181,395, 1),
Point(389,433, 1),
Point(185,385, 1),
Point(387,431, 1),
Point(204,349, 1),
Point(389,438, 1),
Point(199,338, 1),
Point(402,445, 1),
Point(193,335, 1),
Point(402,449, 1),
Point(187,325, 1),
Point(403,454, 1),
Point(171,327, 1),
Point(410,462, 1),
Point(161,327, 1),
Point(415,462, 1),
Point(154,326, 1),
Point(416,461, 1),
Point(150,320, 1),
Point(411,460, 1),
Point(150,317, 1),
Point(405,454, 1),
Point(150,312, 1),
Point(384,427, 1),
Point(151,307, 1),
Point(385,432, 1),
Point(156,304, 1),
Point(385,434, 1),
Point(161,303, 1),
Point(382,428, 1),
Point(169,299, 1),
Point(391,450, 1),
Point(177,289, 1),
Point(404,454, 1),
Point(181,280, 1),
Point(412,460, 1),
Point(187,269, 1),
Point(413,461, 1),
Point(189,260, 1),
Point(415,464, 1),
Point(192,249, 1),
Point(417,466, 1),
Point(197,234, 1),
Point(416,465, 1),
Point(198,220, 1),
Point(416,463, 1),
Point(198,216, 1),
Point(415,463, 1),
Point(198,211, 1),
Point(415,463, 1),
Point(197,206, 1),
Point(415,462, 1),
Point(197,198, 1),
Point(416,462, 1),
Point(197,191, 1),
Point(417,462, 1),
Point(197,183, 1),
Point(417,463, 1),
Point(199,173, 1),
Point(416,464, 1),
Point(199,168, 1),
Point(417,463, 1),
Point(200,162, 1),
Point(415,464, 1),
Point(199,156, 1),
Point(415,464, 1),
Point(195,152, 1),
Point(412,467, 1),
Point(193,145, 1),
Point(411,468, 1),
Point(192,137, 1),
Point(411,468, 1),
Point(191,132, 1),
Point(411,467, 1),
Point(191,130, 1),
Point(410,468, 1),
Point(191,125, 1),
Point(410,468, 1),
Point(192,120, 1),
Point(410,468, 1),
Point(193,114, 1),
Point(410,468, 1),
Point(195,110, 1),
Point(410,468, 1),
Point(196,105, 1),
Point(409,468, 1),
Point(196,104, 1),
Point(406,468, 1),
Point(196,102, 1),
Point(406,468, 1),
Point(196,100, 1),
Point(407,468, 1),
Point(196,98, 1),
Point(408,467, 1),
Point(197,95, 1),
Point(408,467, 1),
Point(197,94, 1),
Point(409,468, 1),
Point(197,91, 1),
Point(409,468, 1),
Point(198,87, 1),
Point(411,468, 1),
Point(198,85, 1),
Point(412,469, 1),
Point(199,83, 1),
Point(412,470, 1),
Point(199,81, 1),
Point(412,470, 1),
Point(200,80, 1),
Point(411,470, 1),
Point(200,79, 1),
Point(411,471, 1),
Point(200,80, 1),
Point(412,471, 1),
Point(200,80, 1),
Point(413,471, 1),
Point(200,80, 1),
Point(413,470, 1),
Point(200,80, 1),
Point(414,470, 1),
Point(200,80, 1),
Point(415,470, 1),
Point(200,79, 1),
Point(416,470, 1),
Point(200,79, 1),
Point(417,470, 1),
Point(200,79, 1),
Point(417,470, 1),
Point(200,78, 1),
Point(417,469, 1),
Point(200,78, 1),
Point(417,469, 1),
Point(200,78, 1),
Point(417,469, 1),
Point(200,77, 1),
Point(416,469, 1),
Point(200,77, 1),
Point(415,469, 1),
Point(197,77, 1),
Point(415,469, 1),
Point(195,79, 1),
Point(415,469, 1),
Point(194,82, 1),
Point(415,469, 1),
Point(191,89, 1),
Point(415,471, 1),
Point(189,96, 1),
Point(414,472, 1),
Point(186,106, 1),
Point(414,473, 1),
Point(182,122, 1),
Point(414,474, 1),
Point(179,133, 1),
Point(415,477, 1),
Point(179,147, 1),
Point(418,477, 1),
Point(178,175, 1),
Point(418,471, 1),
Point(179,189, 1),
Point(418,461, 1),
Point(179,225, 1),
Point(410,461, 1),
Point(171,268, 1),
Point(403,458, 1),
Point(170,283, 1),
Point(394,440, 1),
Point(168,289, 1),
Point(345,390, 1),
Point(169,305, 1),
Point(347,397, 1),
Point(171,313, 1),
Point(344,382, 1),
Point(178,319, 1),
Point(346,382, 1),
Point(183,325, 1),
Point(347,396, 1),
Point(189,330, 1),
Point(350,402, 1),
Point(193,334, 1),
Point(356,401, 1),
Point(199,331, 1),
Point(358,402, 1),
Point(200,334, 1),
Point(361,401, 1),
Point(201,334, 1),
Point(362,402, 1),
Point(201,332, 1),
Point(358,395, 1),
Point(201,333, 1),
Point(365,396, 1),
Point(202,334, 1),
Point(368,400, 1),
Point(201,338, 1),
Point(368,399, 1),
Point(202,337, 1),
Point(368,400, 1),
Point(204,336, 1),
Point(366,394, 1),
Point(204,338, 1),
Point(363,393, 1),
Point(205,338, 1),
Point(354,386, 1),
Point(205,340, 1),
Point(359,401, 1),
Point(202,341, 1),
Point(379,424, 1),
Point(169,390, 1),
Point(379,422, 1),
Point(171,356, 1),
Point(399,429, 1),
Point(160,327, 1),
Point(412,426, 1),
Point(152,322, 1),
Point(426,441, 1),
Point(97,348, 1),
Point(420,452, 1),
Point(82,325, 1),
Point(416,447, 1),
Point(34,379, 1),
Point(421,448, 1),
Point(15,397, 1),
Point(423,446, 1),
Point(-10,389, 1),
Point(423,444, 1),
Point(-16,388, 1),
Point(426,443, 1),
Point(-20,382, 1),
Point(425,442, 1),
Point(-28,390, 1),
Point(426,442, 1),
Point(-26,385, 1),
Point(425,442, 1),
Point(-17,385, 1),
Point(425,441, 1),
Point(-12,389, 1),
Point(425,440, 1),
Point(-5,396, 1),
Point(425,440, 1),
Point(-1,404, 1),
Point(426,440, 1),
Point(0,408, 1),
Point(426,440, 1),
Point(1,409, 1),
Point(426,440, 1),
Point(2,406, 1),
Point(426,437, 1),
Point(4,404, 1),
Point(422,437, 1),
Point(4,404, 1),
Point(421,437, 1),
Point(5,404, 1),
Point(421,437, 1),
Point(6,407, 1),
Point(421,437, 1),
Point(10,408, 1),
Point(421,437, 1),
Point(12,409, 1),
Point(420,437, 1),
Point(14,410, 1),
Point(420,438, 1),
Point(18,411, 1),
Point(420,439, 1),
Point(19,412, 1),
Point(420,440, 1),
Point(19,412, 1),
Point(420,441, 1),
])
recognizer = Recognizer([Drink,Harsh,HarshLeft,Drinkingmobile])

Allpoints=[]









while cap.isOpened():
    # read frame from capture object
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv2.resize(frame, (480, 320))
    framecnt+=1
    try:
        # convert the frame to RGB format
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        print (framecnt)
        # process the RGB frame to get the result
        results = pose.process(RGB)
            # Loop through the detected poses to visualize.
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            print(f"{mp_pose.PoseLandmark(idx).name}: (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")
        
            # Print nose landmark.
        image_hight, image_width, _ = frame.shape
        x=(int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * image_width))
        y=(int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * image_hight))
        
        Allpoints.append(Point(x,y,1))
        x=(int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * image_width))
        y=(int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * image_hight))
        
        Allpoints.append(Point(x,y,1))

        if framecnt%50==0:
              framecnt=0
              print (Allpoints)
              result = recognizer.recognize(Allpoints)
              print (result)
              Allpoints.clear()  
        
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        # show the final output
        cv2.imshow('Output', frame)
        
    except:
            break
    if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()