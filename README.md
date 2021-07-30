
# Attendence System Using OpenCV




## Introduction:-
In the Attendence Systen Using OpenCV the attendence will be marked automatically once the user whose image stored is came infornt of the camera. The attendence marked will be stored in spreadsheet.

The code base is divided into 2 part.

- First part is responsible capturing image and store it into a directory. When the person arrive and sit infront of camera he has to type his name after running the code then webcam will start and your face will be detected then you have to press setted key for capturing imgage(here it is 'q') after then your image will get store with your name provided into the directory and now you can exit from code
- The second part is responsible for marking attendence of the person who will show his face in webcam and if its image is already stored then the code will compare both the images and if encodings matches then it will mark attendence for the person. Once the person attendence is marked it cannot be marked again on same day because its data is being stored and will be compared everytime before marking any perosn attendence


## Installation

- Install python 3.8.3 version 
- Install opencv-python

```bash
  pip install opencv-python
```
- Install numpy

```bash
  pip install numpy
```
- Install boost

```bash
  pip install boost
```
- Install dlib

```bash
  pip install dlib
```
- Install face-recogination

```bash
  pip install face-recogination
```