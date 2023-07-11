import cv2
import mediapipe as mp
from collections import deque
import socket
import time

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the address and port to send the data
address = 'localhost'
port = 12345

# Connect to the receiver script
sock.connect((address, port))

mp_drawing_utils = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)

with mp_hands.Hands(
        max_num_hands=1,
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    # Create a deque to store the most recent labels
    label_history = deque(maxlen=5)

    while cap.isOpened():
        success, image = cap.read()

        if not success:
            break

        # To improve performance, optionally mark the image as not writeable to pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        label = 'Unknown Pose'
        text_color = (0, 0, 255)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing_utils.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
                
                Wrist = [hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y]
                Thumb_cmc = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y]
                Thumb_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y]
                Thumb_ip = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y]
                Thumb_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y]
                Index_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y]
                Index_pip = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y]
                Index_dip = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y]
                Index_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y]
                Middle_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y]
                Middle_pip = [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y]
                Middle_dip = [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y]
                Middle_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y]
                ring_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y]
                ring_pip = [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y]
                ring_dip = [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y]
                ring_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y]
                pinky_mcp = [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y]
                pinky_dip = [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y]
                pinky_pip = [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y]
                pinky_tip = [hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x,hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y]

                mcp_delta_y = abs(pinky_mcp[1] - Index_mcp[1])
                wrist_to_mcp_y = abs(Middle_mcp[1] - Wrist[1])
                wrist_to_mcp_x = abs(Middle_mcp[0] - Wrist[0])
                hands_orient_param = mcp_delta_y/wrist_to_mcp_y
                orient_ratio = wrist_to_mcp_x/wrist_to_mcp_y

                hands_x_side = Wrist[0] - Middle_mcp[0]
                tip_mcp_middle_delta_y = Middle_tip[1]-Middle_mcp[1]
                tip_mcp_middle_delta_x = Middle_tip[0]-Middle_mcp[0]
                
                tip_mcp_index_delta_y = Index_tip[1] - Index_mcp[1]
                tip_mcp_index_delta_x = Index_tip[0] - Index_mcp[0]
                
                tip_pip_middle_delta_x =Middle_tip[0]-Middle_pip[0]
                tip_pip_index_delta_x = Index_tip[0]-Index_pip[0]

            if orient_ratio <0.5:
                if tip_mcp_middle_delta_y >0:
                    if tip_mcp_index_delta_y<0:
                        label = 'D1va, Go Forward'
                    else:
                        label = 'D1va, Turn Around'
                else:
                    label = 'D1va, Go Backward'
            else:
                if hands_x_side <0:
                    #left
                    if tip_pip_middle_delta_x >0:
                        label = 'D1va, Strafe Left'
                    else:
                        if tip_pip_index_delta_x>0:
                            label = 'D1va, Spin Right'
                        else:
                            label = 'D1va, Lay Down'
                
                else:
                    #right
                    if tip_pip_middle_delta_x <0:
                        label = 'D1va, Strafe Right'
                    else:
                        if tip_pip_index_delta_x<0:
                            label = 'D1va, Spin Left'
                        else:
                            label = 'D1va, Stand Up'
                                
        label_history.append(label)  # Add current label to the history

        if label != 'Unknown Pose':
            if len(label_history) == 5 and len(set(label_history)) == 1:
                # Check if the last 5 labels are all equal
                label = label_history[-1]
                text_color = (0, 255, 0)  # Update the color to green for recognized poses
                cv2.putText(image, label, (10, 60), cv2.FONT_HERSHEY_PLAIN, 2, text_color, 2)
                # Send the message
                sock.sendall(label.encode())
        else:
            cv2.putText(image, label, (10, 60), cv2.FONT_HERSHEY_PLAIN, 2, text_color, 2)
            
        cv2.imshow('Pose Classification', image)

        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
# Close the socket
sock.close()