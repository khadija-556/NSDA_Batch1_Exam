from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

def signupPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        display_name = request.POST.get('display_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        user = Custom_User.objects.create_user(username = username, password = password )

        user.display_name =display_name 
        user.email = email
        user.user_type = user_type
    
        user.save()
        if user.user_type == 'recruiter':
            user=RecruiterProfile.objects.create(user=user)
            user.save

        elif user.user_type == 'jobseeker':
            user=JobseekerProfile.objects.create(user=user)
            user.save
        return redirect("signinpage")
    return render(request,"signup.html")

def signinpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)

        if user:
            login(request, user)
            return redirect ("dashboardPage")


    return render(request,"login.html")

def logoutPage(request):
    logout(request)
    return redirect("signinpage")

#@login_required
def dashboardPage(request):

        return render(request,"dashboard.html")
    

#@login_required
def jobviewPage(request):

    job = Job_M.objects.all()
    msg=0
    try:
        if request.GET.get("search"):
            key=request.GET.get("search")
            if Job_M.objects.filter(
                Q(job_title__icontains = key) |
                Q(company_name__icontains = key) |
                Q(job_location__icontains = key)
            ):
                job = Job_M.objects.filter(
                        Q(job_title__icontains = key) |
                        Q(company_name__icontains = key) |
                        Q(job_location__icontains = key)
                        )
            else:
                msg="Not found"
    except:
        return HttpResponse("Not found from except")

    return render (request, "viewjob.html", {'job':job,'msg':msg})

def jobaddPage(request):

    user = request.user

    if request.method == "POST":
        job_title = request.POST.get("job_title")
        company_name = request.POST.get("company_name")
        location = request.POST.get("location")
        description = request.POST.get("description")
        qualification=request.POST.get("qualification")
        company_logo=request.FILES.get("company_logo")
        deadline=request.POST.get("deadline")
      
        job = Job_M(
            job_title = job_title,
            company_name = company_name,
            job_location = location,
            job_description = description,
            qualification=qualification,
            company_logo=company_logo,
            deadline=deadline,

            job_creator = user ,

        )
        job.save()

        return redirect ("jobviewPage")

    return render(request, "recruiter/addjob.html")

def deletejob(request, myid):
    Job_M.objects.filter(id=myid).delete()
    return redirect ("jobviewPage")


def jobIdCall(request, myid):
    job = Job_M.objects.filter(id=myid)
    return render (request, "recruiter/editjob.html", {'job':job})

def editjob(request):

    user = request.user

    if request.method == "POST":
        job_id = request.POST.get("job_id")
        job_title = request.POST.get("job_title")
        company_name = request.POST.get("company_name")
        location = request.POST.get("location")
        description = request.POST.get("description")
        company_logo=request.FILES.get("company_logo")
        # creator = request.POST.get("creator")
        
        job = Job_M(
            id = job_id,
            job_title = job_title,
            company_name = company_name,
            job_location = location,
            job_description = description,
            company_logo=company_logo,
            job_creator = user ,

        )
        job.save()

        return redirect ("jobviewPage")

def applyjobPage(request,myid):

    job=get_object_or_404(Job_M,id=myid)

    if request.method == "POST":
        skills = request.POST.get("Skill")
        phone = request.POST.get("phone")
        photo = request.POST.get("photo")
        address = request.POST.get("address")
        excepted_salay = request.POST.get("excepted_salay")
        signature = request.POST.get("signature")
        cv_cover_latter = request.POST.get("cv_cover_latter")
        cv_apply = request.FILES.get("file")

        if skills and cv_apply:
            job_seeker=request.user
            print(job_seeker)

            application=Jobapply_M.objects.create(
                job=job,
                job_seeker=job_seeker,
                skills=skills,
                phone=phone,
                photo=photo,
                address=address,
                excepted_salay=excepted_salay,
             
                signature=signature,
                cv_cover_latter=cv_cover_latter,

                cv_apply=cv_apply,
            )

            application.save()
            


            return redirect("appliedjobPage")

    return render(request,"job_seeker/applyjob.html")

def appliedjobPage(request):
    user=request.user

    applied_job = Jobapply_M.objects.filter(job_seeker=user)

    return render(request, "job_seeker/appliedjob.html", {'applied_job':applied_job})

def Editappliedjob(request,id):

    return render(request,"job_seeker/Editapplyjob.html")
    

def profilePage(request): 
    return render(request, "profile.html")

def editProfilePage(request):

    user=request.user

    if request.method == "POST":

        user_id=request.POST.get("id")
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        display_name = request.POST.get("display_name")
        about = request.POST.get("about")
        profile_pic=request.FILES.get("profile_pic")
        entered_passwoard =request.POST.get('password')
        skills=request.POST.get("skills")
        cv=request.FILES.get("cv")
        # about =request.POST.get('about')


        if not check_password(entered_passwoard,user.password):
            messages.error(request,'Profile not update,worng password ')


        user.id=user_id
        user.first_name = fname
        user.last_name = lname 
        user.display_name = display_name 
        user.about = about 
        user.skills = skills
        user.cv = cv

        if user.user_type == 'jobseeker':

            try:
                job_seeker_profile = user.khadija
            
            except ObjectDoesNotExist:
                job_seeker_profile=JobseekerProfile(user=user)

          
            job_seeker_profile.skills=skills
            if cv:
                job_seeker_profile.cv=cv
            job_seeker_profile.save()


        if profile_pic:
            user.profile_pic=profile_pic
            
        
        user.save()

        return redirect("profilePage")
        

    return render(request, "editprofile.html")

def changePassord(request):
    user=request.user

    if request.method == 'POST':
        current_pass=request.POST.get("oldPassword")
        newPassword=request.POST.get("newPassword")
        confirmPassword=request.POST.get("confirmPassword")

        if not check_password(current_pass,user.password):
            return redirect("changePassord")
        
        if newPassword != confirmPassword :
            return redirect("changePassord")
        
        user.set_password(newPassword)
        user.save()
        return redirect("signupPage")

    return render(request,'changepassword.html')

def viewjobProfile(request):
    user=request.user
    creator=Job_M.objects.filter(job_creator=user)

    context={
        'creator':creator

    }

    return render(request,'viewjobProfile.html',context)

def applicate(request,id):
    myjob=get_object_or_404(Job_M,id=id)
    job=Jobapply_M.objects.filter(job=myjob)

    context={
        'myjob':myjob,
        'job':job,
    }


    return render(request,"applicate.html",context)






