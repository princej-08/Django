# Generated by Django 4.0.6 on 2022-09-12 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DBOperations', '0004_alter_employee_dept_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-empname']},
        ),
    ]
