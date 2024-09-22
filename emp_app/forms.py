from django import forms
from .models import user,employee,Admin_user,LeaveApplication

class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ['reason']

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ["name","user_type"]  

class adminform(forms.ModelForm):
    class Meta:
        model = Admin_user
        fields = '__all__'

class employeeform(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'