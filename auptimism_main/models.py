from django.db import models

# Create your models here.

class Therapist(models.Model):
    therapist_id=models.AutoField(primary_key=True)
    therapist_name = models.CharField(max_length=255)
    profile_pic=models.FileField()
    phone_no=models.IntegerField()
    email = models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    institute_name=models.CharField(max_length=255)
    Designation=models.CharField(max_length=255)

class Institute(models.Model):
    i_name = models.CharField(max_length=255)
    i_description=models.TextField()
    i_email=models.EmailField()
    i_phone=models.IntegerField()



class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    Father_name = models.CharField(max_length=255)
    Mother_name = models.CharField(max_length=255)
    email_father = models.EmailField()
    email_mother=models.EmailField()
    phoneno_father=models.IntegerField()
    phoneno_mother=models.IntegerField()
    address=models.TextField()
    gender=models.CharField(max_length=255)
    DOB=models.DateField()
    profile_pic=models.FileField()
    Medical_report=models.FileField()
    past_report=models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now_add=True)
    therapist_id=models.ForeignKey(Therapist,on_delete=models.CASCADE)

class IEP(models.Model):
    therapist_name=models.CharField(max_length=255)
    skill=models.CharField(max_length=255)
    therapy_type=models.CharField(max_length=255)

class Activity(models.Model):
    activity_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    tags=models.CharField(max_length=255)
    visibilty = ('Public', 'Private')
    level=models.CharField(max_length=255)
    age=models.IntegerField()
    media=models.FileField()
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)



