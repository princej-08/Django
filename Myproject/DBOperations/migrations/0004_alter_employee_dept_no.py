# Generated by Django 4.0.6 on 2022-09-09 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DBOperations', '0003_department_employee_dept_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DBOperations.department'),
        ),
    ]
