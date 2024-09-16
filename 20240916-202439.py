import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-a13dd-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "012021":
        {
            "name": "Sathya Prakash",
            "major": "AI/Ml",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "123456":
        {
            "name": "Bill Gates",
            "major": "Economics",
            "starting_year": 2024,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "234561":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "456789":
        {
            "name": "Mark Zuckerberg",
            "major": "Data Science",
            "starting_year": 2024,
            "total_attendance": 5,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)