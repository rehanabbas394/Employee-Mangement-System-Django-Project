from django.urls import path
from . import views
urlpatterns = [
    path("index",views.index,name="index"),
    path("register",views.register,name="register"),  
    path("login",views.login_user,name="login"),
    path("about",views.about,name="about"),
    path("term",views.term,name="term"),
    path("condition",views.condition,name="condition"),
    path("contact2",views.contact,name="contact"),
    path("hello",views.hello,name="hello"),
    path("logout",views.logout,name="logout"),
    path("employee_panel", views.employee_panel, name="employee_panel"),
    path("admin_panel", views.admin_panel, name="admin_panel"),
    path('', views.user_register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leave/<int:leave_id>', views.leave_action, name='leave_action'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path("emp_list",views.emp_list,name="employee_list"),
    path("admin_list",views.admin_list,name="admin_list"),
    path("update_emp/<int:id>",views.update_emp,name="update_emp")


]
