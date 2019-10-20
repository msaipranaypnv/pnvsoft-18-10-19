# Generated by Django 2.2.4 on 2019-10-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(default=False)),
                ('board', models.CharField(default=False, max_length=20)),
                ('fatherName', models.CharField(max_length=100)),
                ('motherName', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=30)),
                ('schoolName', models.CharField(max_length=30)),
                ('schoolAddress', models.CharField(max_length=200)),
                ('homeAddress', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=30)),
                ('aadharNumber', models.CharField(max_length=15)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('emailID', models.EmailField(max_length=40)),
                ('personPhoto', models.ImageField(upload_to='images/')),
                ('signaturePhoto', models.ImageField(upload_to='images/')),
                ('username', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
