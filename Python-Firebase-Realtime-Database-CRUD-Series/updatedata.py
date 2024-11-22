import pyrebase

firebaseConfig={"apiKey": "AIzaSyBPhwfUTQqOwKq2xH9087gHEslqEQTSNro",
    "authDomain": "pyrebaserealtimedbdemo.firebaseapp.com",
    "databaseURL": "https://pyrebaserealtimedbdemo.firebaseio.com",
    "projectId": "pyrebaserealtimedbdemo",
    "storageBucket": "pyrebaserealtimedbdemo.appspot.com",
    "messagingSenderId": "843349173643",
    "appId": "1:843349173643:web:90ff345ff844aa89d5fb8e",
    "measurementId": "G-DT093HRL5R"}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()


#Update data with known path
db.child("todolistA").child("monday").child("paper").update({"deadline":"1pm"})
