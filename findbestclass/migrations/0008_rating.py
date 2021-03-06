# Generated by Django 2.1.7 on 2019-02-17 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('findbestclass', '0007_enquiry_admissionstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findbestclass.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findbestclass.Student')),
            ],
        ),
    ]
