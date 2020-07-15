from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyABz0n3otYpBXuPF8q_pS-N0rSwwL98gxc",
    'authDomain': "journal-61748.firebaseapp.com",
    'databaseURL': "https://journal-61748.firebaseio.com",
    'projectId': "journal-61748",
    'storageBucket': "journal-61748.appspot.com",
    'messagingSenderId': "711085520514",
    'appId': "1:711085520514:web:d12efb07ceada86ca9269b"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()

def iep(request):
    date = request.POST.get('date')
    specialist = request.POST.get('specialist[]')
    skills = request.POST.get("Skills")
    print(skills)
    print(specialist)
    Subject=['Language','Mathematics','Language and Communication','Daily Living Skills','Personal health and fitness','Visual Art','Social Skill Development','Assistive Technology']
    data={
        "Learning Exceptations":"should learn 1-100 till this month" ,
        "Teaching Strategies": "data data data",
        "Assessment Method":"data data data",
    }
    data_set={
        "Area of Strength":"motor skills,fine motors",
        "Area of Need":"motor skills,fine motors",
    }
    name="arnika yadav"
    db.child('users').child('Students').child(name).child("IEP").set(data_set)
    for subject in Subject:
        db.child('users').child('Students').child(name).child("IEP").child(subject).set(data)
    return render(request,'iep.html')