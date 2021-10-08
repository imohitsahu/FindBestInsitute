# Generated by Django 2.1.7 on 2019-02-15 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('findbestclass', '0004_institute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=200)),
                ('courseFees', models.IntegerField()),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findbestclass.Institute')),
            ],
        ),
    ]