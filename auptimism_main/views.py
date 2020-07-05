from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
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


def home(request):
    return render(request, 'home.html')


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
        return render(request, 'home.html', {"mssg": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'Dashboard.html')


def show(request):
    return render(request,'Dashboard.html')


def done(request):
    names = request.POST.get("names")
    title = request.POST.get("title")
    heading="ACTIVITY-"+title
    arr_name=names.split(",")
    for i in arr_name:
        db.child('users').child('Students').child(i).child("Activity").push(heading)
    return render(request,'done.html')

def add_profile(request):

    import time
    from datetime import datetime, timezone
    import pytz

    tz= pytz.timezone('Asia/Kolkata')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print(str(time_now).split(" ")[0])

    ProfilePic=request.POST.get('url')
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
    data = request.POST.copy()
    idtoken= request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info"+str(a))
    print(Address)
    first_name = data.get("name")
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

    import time
    from datetime import datetime, timezone
    import pytz

    tz= pytz.timezone('Asia/Kolkata')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili"+str(millis))

    image=request.POST.get('image')
    pdf=request.POST.get('pdf')
    url=request.POST.get('youtube')
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
    skill_req=[]
    i=1
    while i<10:
        skill=request.POST.get("skill_" + str(i))
        if skill is None:
            break
        else:
            skill_req.append(skill)
            i=i+1
    inst_req=[]
    j=1
    while j<10:
        inst=request.POST.get("inst_" + str(j))
        if inst is None:
            break
        else:
            inst_req.append(inst)
            j=j+1


    data = request.POST.copy()
    s=data.getlist("skill_1")
    print(s)

    idtoken= request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info"+str(a))
    Title = data.get("title")
    heading= "ACTIVITY-"+str(Title)
    data = {
        'Title': title,
        'Description': description,
        'Visibility': visibility,
        'Level': Level,
        'age':Age,
        'skill':skill_req,
        "checklist":Checklist,
        "suggestion":suggestion,
        "tags":category,
        "proneeded":Proneeded,
        "instruction":inst_req,
        "url_Youtube":url,
        "video":video,
        "pdf":pdf,
        "image":image,
    }
    db.child('users').child('Activities').child(heading).set(data)
    return render(request,'Uploadactivity.html')


def homeplan(request):
    return render(request,'homeplan.html')

def nochild(request):
    return render(request,'noprofile.html')

def noactivity(request):
    return render(request,'noactivity.html')

def iep(request):
    date = request.POST.get('date')
    specialist = request.POST.get('specialist')
    skills = request.POST.get("skill")
    title_iep = request.POST.get('mytext[]')
    des_iep = request.POST.get('desc[]')
    print(title_iep)
    print(des_iep)
    print(skills)
    return render(request,'iep.html')




def assign(request,title):
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


def view_child(request):
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
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    info = db.child("users").child("Students").child(name).shallow().get().val()
    information2=[]
    information1=[]
    for i in info:
        information1.append(i)
        information2.append(db.child("users").child("Students").child(name).child(i).shallow().get().val())

    information={}
    for j in range(len(information1)):
        information[information1[j]]=information2[j]

    print(information)
    print(information['name'])

    return render(request,'seechild.html',{'information':information})


def show_activity(request):
    q = db.child("users").child("Activities").child().shallow().get().val()
    if not q:
        return render(request,'noactivity.html')
    else:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        users2 = db.child("users").child("Activities").shallow().get().val()
        print(users2)
        titlearr = []


        for i in users2:
            name = db.child("users").child("Activities").child(i).child("Title").shallow().get().val()
            titlearr.append(name)

        print(titlearr)
        return render(request,'homeplan.html' ,{'skillarr':titlearr})


def view_activity(request,title):
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    skill=[]
    checklist=[]
    suggestion=[]
    proneeded=[]
    instruction =[]
    media=[]
    heading="ACTIVITY-"+title
    description=db.child("users").child("Activities").child(heading).child("Description").shallow().get().val()
    Level=db.child("users").child("Activities").child(heading).child("Level").shallow().get().val()
    Visibility=db.child("users").child("Activities").child(heading).child("Visibility").shallow().get().val()
    Age=db.child("users").child("Activities").child(heading).child("age").shallow().get().val()
    Checklist=(db.child("users").child("Activities").child(heading).child("checklist").shallow().get().val()).split("\r")
    instruction=db.child("users").child("Activities").child(heading).child("instruction").get().val()
    proneeded=(db.child("users").child("Activities").child(heading).child("proneeded").shallow().get().val()).split("\r")
    skill=db.child("users").child("Activities").child(heading).child("skill").get().val()
    suggestion=(db.child("users").child("Activities").child(heading).child("suggestion").shallow().get().val()).split("\r")
    youtube=(db.child("users").child("Activities").child(heading).child("url_Youtube").shallow().get().val()).split("=")
    video=db.child("users").child("Activities").child(heading).child("video").shallow().get().val()
    pdf=db.child("users").child("Activities").child(heading).child("pdf").shallow().get().val()
    image=db.child("users").child("Activities").child(heading).child("image").shallow().get().val()
    you="https://www.youtube.com/embed/" + youtube[1]
    if video:
        media.append(video)
    if pdf:
        media.append(pdf)
    if image:
        media.append(image)
    if youtube:
        media.append(you)
    print(media)
    print(description)
    print(Age)
    print(Checklist)
    print(instruction)
    return render(request, 'view_activity.html',{'youtube': media[0],'media':media[1:],'skill':skill,'Level':Level,'Visibility':Visibility,'proneeded':proneeded,'title':title,'d':description,'Age':Age,'checklist':Checklist,'instruction':instruction,'suggestion':suggestion})
