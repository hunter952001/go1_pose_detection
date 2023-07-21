
# go1_pose_classification

control go1 pro robot using hand/body poses using mediapipe
dog password is 00000000


## Authors

- [@hunter952001](https://www.github.com/hunter952001)

- [@TEvettsUF](https://www.github.com/TEvettsUF)

## Using Body Gestures
![Using Body Gestures](https://github.com/hunter952001/go1_pose_detection/assets/85843642/bb78f0c2-2ac9-4ee0-966f-85ccd96f9523)

## Using Hand Gestures
![Using Hand Gestures](https://github.com/hunter952001/go1_pose_detection/assets/85843642/a2c34855-b096-4bbe-b385-11a91f9c1860)

## Installation of Mediapipe

pip install opencv-contrib-python

pip install mediapipe


## Installation of free-dog-sdk (Ubuntu)

cd git

git clone https://github.com/Bin4ry/free-dog-sdk.git

ln -s ~/git/free-dog-sdk/ ~/catkin_ws/src

cd ../catkin_ws

source devel/setup.bash

#Before you install requirements.txt, check your numpy version and edit the txt file

#pip show numpy

cd src/free-dog-sdk

pip install -r requirements.txt

## Installation of free-dog-sdk (Windows)

#Download zip file, extract it in the Documents folder

pip install -r requirements.txt

## How to Use

1. Once the go1 pro is turned on, connect to the robot using your computer's network settings. 
2. In the go1_pose_detection directory, run receiver.py first in its own terminal.
3. Then, in another terminal, run either new_pose.py (for body poses) or new_hands.py (for hand poses). Make sure webacam is setup before running
4. Press Escape on the interface to close
![Screenshot from 2023-07-18 15-15-51](https://github.com/hunter952001/go1_pose_detection/assets/85843642/bf57d017-5ae8-4491-b90f-1bcb41da6e4d)
![talk to the](https://github.com/hunter952001/go1_pose_detection/assets/85843642/707b819b-5088-426f-b133-24ba6957b051)



## Acknowledgements

 - [Bleed AI Academy: Real-Time 3D Pose Detection and Classification](https://www.youtube.com/watch?v=aySurynUNAw)
 - [Bin4ry/free-dog-sdk Github](https://github.com/Bin4ry/free-dog-sdk)
 - [Mediapipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)




