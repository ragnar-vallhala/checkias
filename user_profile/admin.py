from django.contrib import admin
from .models import Student,Coaching,Evaluator,Reviewer,Enquiry,Admin,Superuser
# Register your models here.
#Students
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','attempt']
admin.site.register(Student,StudentModelAdmin)

#Coachings
class CoachingModelAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','attempt']
admin.site.register(Coaching,CoachingModelAdmin)

#Evaluator
admin.site.register(Evaluator)

#Reviewer
admin.site.register(Reviewer)

#Enquiry
admin.site.register(Enquiry)

#Admin
admin.site.register(Admin)

#Superuser
admin.site.register(Superuser)
