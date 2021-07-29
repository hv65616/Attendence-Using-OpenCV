import cv2
import os

#Start the webcam and store the video into a variable
cap = cv2.VideoCapture(0)

#This will read the dataset of frontalface and store that into a variable classifier
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Just a counter to keep record how many images we have captured
count = 0

print("INFO:Capturing Images Process Started")

name = input("Enter your name: ")

#Starting of main code which will be responsible for taking pictures and storing that into a variable
while True:

    #Read the video taken by webcam and store the frames into frame variable
    _, frame = cap.read()

    #Convert the frame from BGR to Grey which will make the detection easier
    convert_to_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #It will use the dataset which we define above and we pass the image or varible which store frame and then it will detect the initial point and the point with height and width and store that 4 values into resized_frame
    resized_frame = classifier.detectMultiScale(convert_to_gray, scaleFactor = 1.2, minNeighbors = 3, minSize = (10, 10))

    #Path which will store our image captured
    path = r'C:\Users\hpw\Desktop\Attendence System Project\Image-Basic'

    #Setting key to zero so that if anyother key apart from clicking pictures clicked it exit from the loop
    key = ord('0')

    #Storing all sepereate values into seperate variable
    for (x, y, w, h) in resized_frame:

        #Draw the rectangle over face we have passed the frame the initial and final point of rectangle and the color of rectangle also the thickness of rectangle
        cv2.rectangle(frame, (x, y), (x+w+50, y+h+100), (0, 255, 0), 2)

        #Will show us the video with rectangle drawn over it
        cv2.imshow("Frame", frame)

        #Not storing the whole frame but cropping the facial part only and storing it
        cropped_image = frame[y:y+h+100,x:x+w+50]

        #Time lap for passing the frames on and if we hit our capturing image key here then it store pressed key value into key variable 
        key = cv2.waitKey(1)

        #Responsible for capture facial part and store inside path mentioned
        if key == ord('q'):

            print("INFO: Capturing...")

            frame_count = "{a}_{b}.jpg".format(a = name,b = count)

            os.chdir(path)

            cv2.imwrite(frame_count,cropped_image)

            count+=1


    #If we press w then we get exit from loop and not doing more image capturing 
    if key == ord('w'):
            
        break

print("INFO:Face Captured Successfully")

cap.release()
cap.destroyAllWindows()
