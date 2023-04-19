import cv2
import os
import pickle
import numpy as np
import face_recognition
import cvzone
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{

    'databaseURL':"https://face-attendence-system-21091-default-rtdb.firebaseio.com/",
    'storageBucket':"face-attendence-system-21091.appspot.com"
})

bucket=storage.bucket()

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
imgBackground=cv2.imread('Resources/background.png')
foldermodepath='Resources/Modes'
modepathlist=os.listdir(foldermodepath)
imgmodelist=[]
#print(modepathlist)
for path in modepathlist:
    imgmodelist.append(cv2.imread(os.path.join(foldermodepath,path)))
#print(len(imgmodelist))

file=open('Encodefile.p','rb')
encodelistknownids=pickle.load(file)
file.close()
encodelistknown,studentsids=encodelistknownids
#print(studentsids)




modeType=0
counter=0
id=-1
imgstudent=[]


ptime=0

while True:
    success,img=cap.read()
    if not success:
        print('Error: Frame not captured')
        break


    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,f'FPS:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
    imgs=cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    facecurrframe=face_recognition.face_locations(imgs)

    encodecurrframe=face_recognition.face_encodings(imgs,facecurrframe)





    imgBackground[162:162+480,55:55+640]=img
    imgBackground[44:44 + 633, 808:808 + 414] =imgmodelist[modeType]
    if facecurrframe:
     for encodeface,faceloc in zip(encodecurrframe,facecurrframe):
        matches=face_recognition.compare_faces(encodelistknown,encodeface)
        facedis=face_recognition.face_distance(encodelistknown,encodeface)
        #print("matches",matches)
        #print("facedis",facedis)
        matchindex=np.argmin(facedis)
        #print("match index",matchindex)
        if matches[matchindex]:
           print("known face detected")
            #print(studentsids[matchindex])

           y1,x2,y2,x1=faceloc
           y1, x2, y2, x1 =y1*4,x2*4,y2*4,x1*4
           bbox=55+x1,162+y1,x2-x1,y2-y1
           imgBackground=cvzone.cornerRect(imgBackground,bbox,rt=0)
           id=studentsids[matchindex]
           if counter==0:
               cvzone.putTextRect(imgBackground,"--Loading 30s",(275,480))
#               cv2.imshow("Face Attendance",imgBackground)
               cv2.waitKey(1)
               counter=1
               modeType=1



     if counter!=0:
        if counter==1:
            studentinfo=db.reference(f'Students/{id}').get()
            print(studentinfo)
            blob=bucket.get_blob(f'Images/{id}.png')
            array=np.frombuffer(blob.download_as_string(), np.uint8)
            imgstudent=cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
            datetimeobject=datetime.strptime(studentinfo['last_attendance_time'],"%Y-%m-%d %H:%M:%S")
            secondselapsed=(datetime.now()-datetimeobject).total_seconds()
            if secondselapsed>30:
                ref = db.reference(f'Students/{id}')
                studentinfo['total_attendance'] += 1
                ref.child('total_attendance').set(studentinfo['total_attendance'])
                ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                modeType=3
                counter=0
                imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[modeType]
        if modeType!=3:
         if 10<counter<20:
            modeType=2
         imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[modeType]
         if counter<=10:
          cv2.putText(imgBackground,str(studentinfo['total_attendance']),(861,125),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)

          cv2.putText(imgBackground, str(studentinfo['major']), (1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (255, 255, 255), 1)
          cv2.putText(imgBackground, str(id), (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (255, 255, 255), 1)
          cv2.putText(imgBackground, str(studentinfo['standing']), (910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                    (100, 100, 100), 1)
          cv2.putText(imgBackground, str(studentinfo['year']), (1025, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                    (100,100,100), 1)
          cv2.putText(imgBackground, str(studentinfo['starting_year']), (1125, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                    (100, 100, 100), 1)


          (w,h),_=cv2.getTextSize(studentinfo['name'],cv2.FONT_HERSHEY_COMPLEX,1,1)
          offset=(414-w)//2

          cv2.putText(imgBackground, str(studentinfo['name']), (808+offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (50, 50, 50), 1)
          imgBackground[175:175+216,909:909+216]=imgstudent
         counter+=1
         if counter>=20:
            counter=0
            modeType=0
            studentinfo=[]
            imgstudent=[]
            #imgBackground[44:44 + 633, 808:808 + 414] = imgmodelist[modeType]

     else:
         modeType=0
         counter=0



   # cv2.imshow("webcam",img)
    cv2.imshow("face attebdence",imgBackground)
    cv2.waitKey(10)
