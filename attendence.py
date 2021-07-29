import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#path variable store the name of folder where our image is stored
path = 'Image-Basic'

#images is a empty list which will store all the images into it
images = []

#imagesName is a empty list which will only store the name of images
imagesName = []

#myImagesList will store all the images present in folder Image-Basic into it and print the image list onto console
myImagesList = os.listdir(path)
print(myImagesList)

#This part of code is responsible for reading image name from myImagesList and store the image into images list and name of image into imagesName list after that display imagesName list onto console
for cl in myImagesList:
    currentImage = cv2.imread(f'{path}/{cl}')
    images.append(currentImage)
    imagesName.append(os.path.splitext(cl)[0])
print(imagesName)

#Now this part of code is responsible for finding the encoding of image stored in image list and store that encodings into another list i.e imageEncoding after that return that stored encoding list
def findEncoding(images):
    imageEncoding = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        imageEncoding.append(encode)
    return imageEncoding

# The below code is reponsible for marking attendence which will take name as a input inside function and mark the attendence 
# First it will open tht .csv file in write mode and read all the date stored inside it and store it into myDataList
# After then from myDataList we will store the names into nameList list by spliting the line with comma(,)
# And then check whether the name is alredy present inside list or not if not then make his/her attendence and it present then leave it
def markAttendence(name):
    with open('Attendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            timeString = now.strftime('%H:%M:%S')
            dateString = now.date()
            f.writelines(f'{name},{timeString},{dateString}\n')

#This will store the imgaeEncoding list into a variable imageEncodingKnown
imageEncodingKnown = findEncoding(images)

#This will print the message
print("Encoding Completed")

#Start the webcam and store the video input into cap
cap = cv2.VideoCapture(0)

#Starting of loop
while True:

    #After reading video we will store two things first the frames into frame variable and second yes/no into success 
    success, frame = cap.read()

    #Here, we are making the size of frame small i.e 1/4th of original frame size
    frameSmall = cv2.resize(frame, (0, 0), None, 0.25, 0.25)

    #And conerting it into BGR to RGB
    frameSmall = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2RGB)

    #Now we will find the face location of frameSmall and store that into faesCurrFrame
    facesCurrFrame = face_recognition.face_locations(frameSmall)

    #After finding the location we will find its encodings and there we pass both framesmall and facesCurrFrame and store that encodings into encodesCurrFrame
    encodesCurrFrame = face_recognition.face_encodings(frameSmall, facesCurrFrame)

    #Below for loop will take facesCurrFrame,encodesCurrFrame and store the values into two seperate variable 
    #After that we will compare both the encodings i.e imageEncodingKnown and encoding that we just found out and store the output of it into matches and also find the distance between two
    #And this distance will provide us the index of image 
    for encodeFace, faceLocation in zip(encodesCurrFrame, facesCurrFrame):
        matches = face_recognition.compare_faces(imageEncodingKnown, encodeFace)
        faceDistance = face_recognition.face_distance(imageEncodingKnown, encodeFace)
        matchIndex = np.argmin(faceDistance)

        #Now if the match is true and image is present in that location then we will store the name of image into name variable by passing the index into imagesName
        #After that make the size of frame original and draw a rectangle on face along with that display the name who is this person
        #And at last call markAttendence function to mark the attendence    
        if matches[matchIndex]:
            name = imagesName[matchIndex].upper()
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2+30, y2+60), (0, 255, 0), 2)
            # cv2.rectangle(frame, (x1, y1), (x2-30, y2-30), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, name, (x1, y2+50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
            markAttendence(name)
    
    #Show the live preview of webcam to user
    cv2.imshow("Webcam", frame)

    #Setting of timeinterval for frames to repeat itself
    key = cv2.waitKey(1)

    #This condition is for breaking out of loop
    if key == ord('q'):
        break


cap.release()

cap.deleteAllWindows()


#*******************************************************Marking Attendence Of A Person Using OpenCV And Computer Vision*******************************************************#
