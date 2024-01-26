from django.db import models

from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER = [
        ('recruiter','Recuriter'),
        ('jobseeker','JobSeeker'),
    ]

    display_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    user_type = models.CharField(choices=USER , max_length=100)
    profile_pic = models.ImageField(upload_to= "media/profile_pic" , null= True)
    about=models.TextField(null=True)
   

    def __str__(self):
        return self.display_name

class Job_M (models.Model):
    job_title = models.CharField(max_length=100, null= True)
    company_name = models.CharField(max_length=100 , null= True)
    job_location = models.CharField(max_length=100 , null= True)
    job_description = models.TextField(null =True)
    create_at = models.DateTimeField(auto_now_add=True, null =True)
    qualification=models.TextField(max_length=100, null=True)
    company_logo= models.ImageField(upload_to= "media/company_logo" , null= True)
    deadline=models.DateField(auto_now_add=True, null =True)
    job_creator = models.ForeignKey(Custom_User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title
    
class Jobapply_M (models.Model):
    job_seeker = models.ForeignKey(Custom_User, on_delete=models.CASCADE, null =True , blank =True)
    job = models.ForeignKey(Job_M,on_delete = models.CASCADE , null =True , blank =True)
    skills=models.CharField(max_length=100 , null=True)
    phone=models.CharField(max_length=100 , null=True)
    photo=models.ImageField(upload_to= "media/photo" , null= True)
    address=models.CharField(max_length=100,null=True)
    excepted_salay=models.CharField(max_length=100,null=True)
    signature=models.ImageField(upload_to= "media/signature" , null= True)
    cv_cover_latter=models.TextField(null=True)
    cv_apply = models.FileField(upload_to= "media/cv_apply" , null= True)

    
class RecruiterProfile(models.Model):
    user = models.OneToOneField(Custom_User,null=True, on_delete = models.CASCADE, related_name='recruiter')
    


    def __str__(self):
        return self.user.display_name

class JobseekerProfile(models.Model):

    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='khadija')
    skills=models.TextField(max_length=100 , null=True)
    cv = models.FileField(upload_to= "media/cv" , null= True)

    def __str__(self):
        return self.user.display_name
    