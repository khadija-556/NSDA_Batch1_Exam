from django.contrib import admin

from .models import *

class Custom_User_Display (admin.ModelAdmin):
    list_display=['display_name', 'email', 'user_type']

class Job_M_Display (admin.ModelAdmin):
    list_display=['job_title', 'company_name', 'job_location']


admin.site.register(Custom_User,Custom_User_Display)
admin.site.register(Job_M,Job_M_Display)
admin.site.register(Jobapply_M)
admin.site.register(RecruiterProfile)
admin.site.register(JobseekerProfile)
