import cv2 #for image processsing
import numpy as np
import face_recognition
import os #for loading images
import streamlit as st
from datetime import datetime
import pandas as pd
from storage import *
from show_stats import *

def record_attendance():
    st.title("Record Attendance")
    st.info("Please align your face in front of the camera.")
    run=st.checkbox("Start Camera")
    FRAME_WINDOW=st.image([])  #an empty list for unknown camera output
    path='images'
    images=[] #list
    PersonName=[] #list
    myList=os.listdir(path) #list containing image names
    #print(myList) #printing image names i.e the list

    #to get the image names and to append these names to defined lists
    for cu_img in myList:
        current_image=cv2.imread(f'{path}/{cu_img}') #reading the image and storing its path
        images.append(current_image)
        PersonName.append(os.path.splitext(cu_img)[0]) #spliiting the image names to remove .jpg
    #print(PersonName)

    #to mark the encoding of images in the dataset
    def faceEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #changing the color code for proper image processing
            encode=face_recognition.face_encodings(img)[0] #using function of face recognition package to prepare encoding of images
            encodeList.append(encode)
        return encodeList

           
    encodeList2=faceEncodings(images)
    print("Encoding complete!")

    caps = cv2.VideoCapture(0)

    while run:
        ret, frame= caps.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = cv2.resize(frame, (0,0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        faces_current_frame= face_recognition.face_locations(faces)
        encode_current_frame=face_recognition.face_encodings(faces, faces_current_frame)

        for encodeface, facelocation in zip(encode_current_frame, faces_current_frame,):
            matches = face_recognition.compare_faces(encodeList2, encodeface)
            facedistance= face_recognition.face_distance(encodeList2, encodeface)

            matchindex= np.argmin(facedistance) 
            if matches[matchindex]:
                name=PersonName[matchindex].upper()
                val=name
                y1, x2, y2, x1= facelocation
                y1, x2, y2, x1= y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.rectangle(frame, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(frame, name, (x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                store_attendance(name)
                view=st.checkbox("Click here to view your monthly statistics")
                if view:
                    stats(name)
                
        FRAME_WINDOW.image(frame)
        
        break

    

               
                
                
                
        
        
    
   


        



        