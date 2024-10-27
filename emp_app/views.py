from django.shortcuts import render, redirect,Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contact , user,employee,Admin_user,LeaveApplication
from .forms import UserForm,adminform,employeeform,LeaveApplicationForm
from django.urls import reverse
from Employee_management_system import settings
from django.core.mail import send_mail


def index(request):
    return render(request, "html/index.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1)
                user.first_name = fname
                user.last_name = lname
                user.save()
                messages.success(request, "Your account has been successfully created")
                
                #email system
                
                # subject ="WellCome to Employee Management System"
                # message = "Hello" + user.first_name + "!! \n" + "Wellcome to Employee Management System!! \n Thanks for visiting our websites \n  We have also sent you a confirmation email, pleasue confirm your email in order to activate your accounts \n Thanks you\n\n Rehan Abbas"
                # from_email = settings.EMAIL_HOST_USER
                # to_list=[user.email]
                # send_mail(subject,message,from_email,to_list)
                 
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")

    return render(request, "html/register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, "html/hello.html",{"fname": fname})
        else:
            messages.error(request, "Bad Credential")
            return redirect('register')

    return render(request, "html/login.html")

def hello(request):
    return render(request, "html/hello.html")


def logout(request):
    logout(request)
    messages.success(request,"you are successfully logged out")
    redirect("register")



def about(request):
    return render(request, "html/about.html")

def term(request):
    return render(request, "html/term.html")

def condition(request):
    return render(request, "html/condition.html")

def contact(request):
    if request.method =="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return render(request, 'html/contact.html', {'status': 'Message sent successfully!'})
    return render(request, "html/contact.html")


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = user.user_type
            if user_type == 'admin':
                return redirect(reverse('admin_panel'))
            else:
                return redirect(reverse('employee_panel'))
    else:
        form = UserForm()
    
    context = {'form': form}
    return render(request, 'html/user.html', context)


def employee_panel(request):
    if request.method == "POST":
        form = employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = employeeform()
    context = {'form': form}
    return render(request, "html/emp_panal.html", {'form': form})

    
def admin_panel(request):
    if request.method == 'POST':
        form = adminform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = adminform()
    return render(request, "html/admin_panal.html", {'form': form})


@login_required
def dashboard(request):
    """Redirect to employee or admin dashboard based on user profile"""
    if request.user.userprofile.is_employee:
        return employee_dashboard(request)
    else:
        return admin_dashboard(request)

@login_required
def employee_dashboard(request):
    """Employee dashboard view"""
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            leave_application = form.save(commit=False)
            leave_application.employee = request.user
            leave_application.save()
    else:
        form = LeaveApplicationForm()
    leave_applications = LeaveApplication.objects.filter(employee=request.user)
    return render(request, 'html/employee_dashboard.html', {'form': form, 'leave_applications': leave_applications})

@login_required
def admin_dashboard(request):
    """Admin dashboard view"""
    leave_applications = LeaveApplication.objects.all()
    return render(request, 'html/admin_dashboard.html', {'leave_applications': leave_applications})

@login_required
def leave_action(request, leave_id: int):
    """Leave action view (accept/reject)"""
    if leave_id is None:
        raise Http404("Leave ID is required")
    leave_application = LeaveApplication.objects.get(pk=leave_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            leave_application.status = 'accepted'
        elif action == 'reject':
            leave_application.status = 'rejected'
        leave_application.save()
    return render(request, 'html/leave_action.html', {'leave_application': leave_application})


def emp_list(request):
    form = employee.objects.all()
    return render(request, "html/emp_list.html",{"form":form})

def admin_list(request):
    form = employee.objects.all()
    return render(request,"html/adm_list.html",{"form":form})

def update_emp(request,id):
    data = employee.objects.get(id=id)
    form = employeeform(instance=data)
    if request.method == "POST":
        form = employeeform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("admin_list")
    return render(request,"html/update_emp.html",{"form":form})