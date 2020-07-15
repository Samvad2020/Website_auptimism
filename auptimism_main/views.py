from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import pyrebase
from django.contrib import auth

'''
import os
os.getenv()
'''
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


def home(request):
    return render(request, 'home.html')

#logout
def logout(request):
    auth.logout(request)
    return render(request, 'home.html')


def login(request):
    # check if a user exists
    # with thr username and password
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    try:
        user = authe.sign_in_with_email_and_password(email, pwd)
    except:
        message = "Invalid Credentials"
        return redirect(request, 'home.html', {"mssg": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'Dashboard.html')


def show(request):
    return render(request,'Dashboard.html')


def add_profile(request):
    #add child profile function
    import time
    from datetime import datetime, timezone
    import pytz

    tz= pytz.timezone('Asia/Kolkata')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print(str(time_now).split(" ")[0])

    ProfilePic=request.POST.get('url')
    Profile=request.POST.get('files[]')
    print(Profile)
    Name_of_child=request.POST.get("name")
    Gender=request.POST.get('gender')
    DOB=request.POST.get('dateofbirth')
    Address=request.POST.get("Address")
    Street=request.POST.get("street")
    State=request.POST.get("state")
    Pincode=request.POST.get("pincode")
    Mothername=request.POST.get("mothername")
    Fathername=request.POST.get("fathername")
    emailmother=request.POST.get("emailmother")
    emialfather=request.POST.get("emailfather")
    phonemother=request.POST.get("phonemother")
    phonefather=request.POST.get("phonefather")
    diagnosis=request.POST.get("diagnosis")
    medical_condition=request.POST.get("medicalcondition")
    medication=request.POST.get("medication")
    rdaignosis=request.POST.get("url1")
    rmedical_condition =request.POST.get("url2")
    rmedication=request.POST.get("url3")
    data_ = request.POST.copy()
    idtoken= request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info"+str(a))
    print(Address)
    first_name = data_.get("name")
    #first_name=first_name.lower()

    data = {

        "profilepic":ProfilePic,
        "name":Name_of_child,
        "Gender":Gender,
        "DOB":DOB,
        "Address":Address,
        "Street":Street,
        "State":State,
        "Pincode":Pincode,
        "Mothername":Mothername,
        "Fathername":Fathername,
        "Emailmother":emailmother,
        "Emailfather":emialfather,
        "Phonemother":phonemother,
        "Phonefather":phonefather,
        "diagnosis":diagnosis,
        "medical_condition":medical_condition,
        "medication":medication,
        "rdiagnosis":rdaignosis,
        "rmedicalcondition":rmedical_condition,
        "rmedication":rmedication
    }
    db.child('users').child('Students').child(first_name).set(data)

    return render(request,'addchild.html')


def create_activity(request):
    #create activity function
    import time
    from datetime import datetime, timezone
    import pytz

    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili" + str(millis))
    data = request.POST.copy()
    image = request.POST.get('image')
    pdf = request.POST.get('pdf')
    url = request.POST.get('youtube')
    video = request.POST.get('url')
    description = request.POST.get('description')
    visibility = request.POST.get('mode')
    title = request.POST.get('title')
    suggestion = request.POST.get('tips')
    Checklist = request.POST.get('checklist')
    Proneeded = request.POST.get('proneeded')
    Age = request.POST.get('age')
    category = request.POST.get('tags')
    Level = request.POST.get('level')
    Duration = request.POST.get('Duration')

    skill_req = []
    i = 1
    while i < 10:
        skill = request.POST.get("skill_" + str(i))
        if skill is None:
            break
        else:
            skill_req.append(skill)
            i = i + 1
    inst_req = []
    j = 1
    while j < 10:
        inst = request.POST.get("inst_" + str(j))
        if inst is None:
            break
        else:
            inst_req.append(inst)
            j = j + 1

    s = data.getlist("skill_1")
    print(s)

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info" + str(a))
    Title = data.get("title")
    heading = "ACTIVITY-" + str(Title)
    data = {
        'Title': title,
        'Description': description,
        'Visibility': visibility,
        'Level': Level,
        'age': Age,
        'skill': skill_req,
        "suggestion": suggestion,
        "tags": category,
        "proneeded": Proneeded,
        "instruction": inst_req,
        "url_Youtube": url,
        "video": video,
        "pdf": pdf,
        "image": image,
        "Duration": Duration,
        "Checklist": Checklist
    }

    db.child('users').child('Activities').child(heading).set(data)
    return render(request,'Uploadactivity.html')


def homeplan(request):
    return render(request,'homeplan.html')


def nochild(request):
    return render(request,'noprofile.html')


def noactivity(request):
    return render(request,'noactivity.html')


def assign(request,title):
    #page which shows child profile
    q = db.child("users").child("Students").child().shallow().get().val()
    if not q:
        return render(request, 'noprofile.html')
    else:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        users1 = db.child("users").child("Students").shallow().get().val()
        namearr = []
        picarr = []
        for i in users1:
            name = db.child("users").child("Students").child(i).child("name").shallow().get().val()
            pic = db.child("users").child("Students").child(i).child("profilepic").shallow().get().val()
            namearr.append(name)
            picarr.append(pic)

        comp_list = zip(namearr, picarr)

        return render(request, 'Assignactivity.html', {'comp_list': comp_list, 'title':title})


def done(request):
    #function to push activity in individual child profile (one activtiy assigned to multiple child)
    names = request.POST.get("names")
    title = request.POST.get("title")
    heading = "ACTIVITY-"+title
    #get the checklist in the form of array
    Checklist = (db.child("users").child("Activities").child(heading).child("Checklist").shallow().get().val()).split("\r\n")
    arr_name=names.split(",")
    data={

        "progress":0,
        "comments":" ",
    }
    prompt={
        "DoneAssitance":False,
        "DonePrompt":False,
        "DoneOwn":False,
    }
    for assigned_child_name in arr_name:
        assigned_child_name=assigned_child_name.lower()
        db.child('users').child('Students').child(assigned_child_name).child("Activity").child(heading).set(data)
        for step in Checklist:
            db.child('users').child('Students').child(assigned_child_name).child("Activity").child(heading).child("checklist").child(step).set(prompt)
    return render(request, 'done.html')


def view_child(request):
    #view child profiles which are created under student profile columns
    q = db.child("users").child("Students").child().shallow().get().val()
    if not q:
        return render(request, 'noprofile.html')
    else:
        users1 = db.child("users").child("Students").shallow().get().val()
        print(users1)
        namearr = []
        picarr = []
        for i in users1:
            name = db.child("users").child("Students").child(i).child("name").shallow().get().val()
            pic = db.child("users").child("Students").child(i).child("profilepic").shallow().get().val()
            namearr.append(name)
            picarr.append(pic)

        comp_list = zip(namearr, picarr)
        return render(request, 'view_child.html', {'comp_list': comp_list})


def seechild(request,name):
    #view complete child info
    idtoken = request.session['uid']

    name=name.lower()
    info = db.child("users").child("Students").child(name).shallow().get().val()
    information2=[]
    information1=[]
    for i in info:
        information1.append(i)
        information2.append(db.child("users").child("Students").child(name).child(i).shallow().get().val())

    information={}
    for j in range(len(information1)):
        information[information1[j]]=information2[j]

    #print(information)
    #print(information['name'])

    return render(request,'seechild.html',{'information':information})


def show_activity(request):
    q = db.child("users").child("Activities").child().shallow().get().val()
    if not q:
        return render(request,'noactivity.html')
    else:
        idtoken = request.session['uid']
        users2 = db.child("users").child("Activities").shallow().get().val()
        print(users2)
        titlearr = []
        for i in users2:
            name = db.child("users").child("Activities").child(i).child("Title").shallow().get().val()
            titlearr.append(name)

        print(titlearr)
        return render(request,'homeplan.html' ,{'skillarr':titlearr})



def view_activity(request,title):
    import re
    idtoken = request.session['uid']
    media=[]
    heading="ACTIVITY-"+title
    description=db.child("users").child("Activities").child(heading).child("Description").shallow().get().val()
    duration=db.child("users").child("Activities").child(heading).child("Duration").shallow().get().val()
    Level=db.child("users").child("Activities").child(heading).child("Level").shallow().get().val()
    Visibility=db.child("users").child("Activities").child(heading).child("Visibility").shallow().get().val()
    Age=db.child("users").child("Activities").child(heading).child("age").shallow().get().val()
    Checklist=(db.child("users").child("Activities").child(heading).child("Checklist").shallow().get().val()).split("\r\n")
    instruction=db.child("users").child("Activities").child(heading).child("instruction").get().val()
    proneeded=(db.child("users").child("Activities").child(heading).child("proneeded").shallow().get().val()).split("\r\n")
    skill=db.child("users").child("Activities").child(heading).child("skill").get().val()
    suggestion=(db.child("users").child("Activities").child(heading).child("suggestion").shallow().get().val()).split("\r\n")
    youtube=db.child("users").child("Activities").child(heading).child("url_Youtube").shallow().get().val()
    video=db.child("users").child("Activities").child(heading).child("video").shallow().get().val()
    pdf=db.child("users").child("Activities").child(heading).child("pdf").shallow().get().val()
    image=db.child("users").child("Activities").child(heading).child("image").shallow().get().val()
    if youtube:
        result = re.match('^[^v]+v=(.{11}).*', youtube)
        you=result.group(1)
    if video:
        media.append(video)
    if pdf:
        media.append(pdf)
    if image:
        media.append(image)
    if youtube:
        media.append("https://www.youtube.com/embed/" +str(you))
    print(media)
    print(description)
    print(Age)
    print(Checklist)
    print(instruction)
    return render(request, 'view_activity.html',{'youtube': media[0],'media':media[0:],'skill':skill,'Level':Level,'Visibility':Visibility,'proneeded':proneeded,'title':title,'d':description,'Age':Age,'checklist':Checklist,'instruction':instruction,'suggestion':suggestion,'duration':duration})


def report(request,name):
    medication=db.child("users").child("Students").child(name).child("rmedication").shallow().get().val()
    return render(request, 'report.html',{'m':medication})

def reportd(request,name):
    diagnois=db.child("users").child("Students").child(name).child("rdiagnosis").shallow().get().val()
    return render(request, 'reportd.html',{'d':diagnois})

def reportmed(request,name):
    medical=db.child("users").child("Students").child(name).child("rmedical_condition").shallow().get().val()
    return render(request, 'reportmed.html', {'med': medical})

def contact(request):
    import time
    from datetime import datetime, timezone
    import pytz
    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))

    email_id = request.POST.get('email')
    Message = request.POST.get('Message')
    data={
        "Email_ID":email_id,
        "Message":Message,
    }
    db.child('users').child('QUERIES').child(millis).set(data)
    return render(request,'contact.html')