# Generated by Django 4.0.6 on 2022-08-28 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DBOperations', '0002_employee_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('deptname', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='dept_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DBOperations.department'),
        ),
    ]