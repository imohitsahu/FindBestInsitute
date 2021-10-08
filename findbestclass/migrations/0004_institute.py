# Generated by Django 2.1.7 on 2019-02-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findbestclass', '0003_auto_20190215_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adminName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('landmark', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=30)),
                ('lng', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]