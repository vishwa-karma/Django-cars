# Generated by Django 2.2.7 on 2019-11-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
