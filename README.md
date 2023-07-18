
# go1_pose_classification

control go1 pro robot using hand/body poses using mediapipe


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

## Acknowledgements

 - [Bleed AI Academy: Real-Time 3D Pose Detection and Classification](https://www.youtube.com/watch?v=aySurynUNAw)
 - [Bin4ry/free-dog-sdk Github](https://github.com/Bin4ry/free-dog-sdk)




