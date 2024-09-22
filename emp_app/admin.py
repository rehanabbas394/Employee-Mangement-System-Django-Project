from django.contrib import admin
from . models import Contact,user,employee,Admin_user,LeaveApplication,UserProfile

@admin.register(Contact)
class contactadmin(admin.ModelAdmin):
    list_display =["id","name","email","message"] 

@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display =["id","name","user_type"]

@admin.register(employee)
class employeeadmin(admin.ModelAdmin):
    list_display =["id","name","email","dep","role","contact","address","salary","user"]
  
@admin.register(Admin_user)  
class Admin_user(admin.ModelAdmin):
    list_display =["id","name","email","contact","address"]
    
@admin.register(LeaveApplication)
class LeaveApplicationadmin(admin.ModelAdmin):
    list_display =["employee","reason","status_choices","status","date_created"]
    
    
@admin.register(UserProfile)
class UserProfileadmin(admin.ModelAdmin):
    list_display =["user","is_employee"]