import cv2
import os
import face_recognition
import _pickle
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{

    'databaseURL':"https://face-attendence-system-21091-default-rtdb.firebaseio.com/",
    'storageBucket':"face-attendence-system-21091.appspot.com"
})
foldermodepath='Images'
modepathlist=os.listdir(foldermodepath)
imgmodelist=[]
studentids=[]
#print(modepathlist)

for path in modepathlist:
    imgmodelist.append(cv2.imread(os.path.join(foldermodepath,path)))
   # print(path)
    #print(os.path.splitext(path)[0])
    studentids.append(os.path.splitext(path)[0])
    fileName=f'{foldermodepath}/{path}'
    bucket=storage.bucket()
    blob=bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentids)

def findencoding(imageslist):
    encodelist=[]
    for img in imageslist:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
encodelistknown=findencoding(imgmodelist)
print(encodelistknown)
encodelistknownids=[encodelistknown,studentids]
print("encoding complete")
file=open("Encodefile.p",'wb')
pickle.dump(encodelistknownids,file)
file.close()
print("file saved")
