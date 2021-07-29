import cv2
import numpy as np
import face_recognition

imageElon = face_recognition.load_image_file('Image-Basic/Elon1.jpg')
imageElon = cv2.cvtColor(imageElon,cv2.COLOR_BGR2RGB)
imageElonTest = face_recognition.load_image_file('Image-Basic/Elon2.jpg')
imageElonTest = cv2.cvtColor(imageElonTest,cv2.COLOR_BGR2RGB)

faceLocation = face_recognition.face_locations(imageElon)[0]
encodeElon = face_recognition.face_encodings(imageElon)[0]
cv2.rectangle(imageElon,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(0,255,0),2)

faceLocationTest = face_recognition.face_locations(imageElonTest)[0]
encodeElonTest = face_recognition.face_encodings(imageElonTest)[0]
cv2.rectangle(imageElonTest,(faceLocationTest[3],faceLocationTest[0]),(faceLocationTest[1],faceLocationTest[2]),(56,255,188),2)

results = face_recognition.compare_faces([encodeElon],encodeElonTest)
faceDistance = face_recognition.face_distance([encodeElon],encodeElonTest)
print(results)
print(faceDistance)
cv2.putText(imageElon,f'{results} {round(faceDistance[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,188),2)

cv2.imshow("Elon1",imageElon)
cv2.imshow("Elon2",imageElonTest)
cv2.waitKey(0)