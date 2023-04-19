
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{

    'databaseURL':"https://face-attendence-system-21091-default-rtdb.firebaseio.com/"
})
ref=db.reference('Students')
data={
    "321654":{
        "name":"Dasvir Singh",
        "major":"Robotics",
        "starting_year":"2021",
        "total_attendance":16,
        "standing":"G",
        "year":2,
        "last_attendance_time":"2022-12-11 00:54:34"
    },
    "852741": {
        "name": "Emly Blunt",
        "major": "Mathematics",
        "starting_year": "2015",
        "total_attendance": 16,
        "standing": "B",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": "2020",
        "total_attendance": 12,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
    "102117011": {
        "name": "Ashmandeep",
        "major": "Physics",
        "starting_year": "2020",
        "total_attendance": 12,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
    "102117006": {
        "name": "Parasinder singh",
        "major": "biology",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
    "102117034": {
       "name": "Shivam aggarwal",
        "major": "chemistry",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
"102117024": {
       "name": "Daksh tyagi",
        "major": "mechanics",
        "starting_year": "2021",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
"102117021": {
       "name": "pranjali sharma",
        "major": "chemistry",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
"102117029": {
       "name": "Ambreesh",
        "major": "chemistry",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
"102117031": {
       "name": "jasmeen",
        "major": "chemistry",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
"102117007": {
       "name": "Shubham ghandhi",
        "major": "chemistry",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
"102117017": {
       "name": "ikshan bhardwraj",
        "major": "cp",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
"102117023": {
       "name": "joy goswami",
        "major": "AI",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },
"102117030": {
       "name": "Yahash garag",
        "major": "machine",
        "starting_year": "2020",
        "total_attendance": 1,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2020-12-11 00:54:34"
    },

}
for key,value in data.items():
    ref.child(key).set(value)