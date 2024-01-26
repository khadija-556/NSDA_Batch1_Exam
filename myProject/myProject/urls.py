
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signinpage',signinpage, name="signinpage"),
    path('',signupPage, name="signupPage"),
    path('logoutPage/',logoutPage, name="logoutPage"),
    path('dashboardPage/',dashboardPage, name="dashboardPage"),
    path('jobviewPage/',jobviewPage, name="jobviewPage"),
    path('jobaddPage/',jobaddPage, name="jobaddPage"),
    path('deletejob/<str:myid>',deletejob, name="deletejob"),
    path('jobIdCall/<str:myid>',jobIdCall, name="jobIdCall"),
    path('editjob/',editjob, name="editjob"),
    path('applyjobPage/<str:myid>',applyjobPage, name="applyjobPage"),
    path('appliedjobPage/',appliedjobPage, name="appliedjobPage"),
    path('Editappliedjob/<str:id>',Editappliedjob, name="Editappliedjob"),
    path('profilePage/',profilePage, name="profilePage"),
    path('editProfilePage/',editProfilePage, name="editProfilePage"),
    path('applicate/<str:id>',applicate, name="applicate"),
    path('changePassord/',changePassord, name="changePassord"),
    path('viewjobProfile/',viewjobProfile, name="viewjobProfile"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
