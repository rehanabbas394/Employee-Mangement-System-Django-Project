# Generated by Django 5.0.4 on 2024-05-12 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0005_leaveapplication_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dep',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(default=True, max_length=100, null=True),
        ),
    ]
