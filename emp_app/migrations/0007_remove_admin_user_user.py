# Generated by Django 5.0.4 on 2024-05-12 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0006_employee_dep_employee_role_alter_employee_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_user',
            name='user',
        ),
    ]
