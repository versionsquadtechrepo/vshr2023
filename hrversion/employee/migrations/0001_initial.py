# Generated by Django 3.2.18 on 2023-04-13 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('util', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationname', models.CharField(max_length=64)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('revisionname', models.CharField(max_length=64)),
                ('revisiondate', models.DateTimeField(auto_now=True)),
                ('user_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='util.gender')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationname', models.CharField(max_length=64)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('revisionname', models.CharField(max_length=64)),
                ('revisiondate', models.DateTimeField(auto_now=True)),
                ('password', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=100)),
                ('login_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='util.logintype')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='util.status')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
