# Generated by Django 2.1.7 on 2019-02-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findbestclass', '0006_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='admissionStatus',
            field=models.IntegerField(default=0),
        ),
    ]
