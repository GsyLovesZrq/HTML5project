# Generated by Django 2.0.7 on 2018-08-22 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('checkID', models.AutoField(primary_key=True, serialize=False)),
                ('startUpTime', models.CharField(max_length=20)),
                ('duration', models.IntegerField()),
                ('enable', models.BooleanField(default=True)),
                ('results', models.CharField(max_length=1000)),
                ('members', models.CharField(max_length=1000)),
                ('startDate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='checkPlan',
            fields=[
                ('planID', models.AutoField(primary_key=True, serialize=False)),
                ('startUpTime', models.CharField(max_length=20)),
                ('duration', models.IntegerField()),
                ('repeat', models.CharField(max_length=20)),
                ('enable', models.BooleanField(default=False)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('groupID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('member', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('passwd', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=10)),
                ('profile', models.CharField(max_length=100)),
                ('userType', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.user'),
        ),
        migrations.AddField(
            model_name='checkplan',
            name='groupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.group'),
        ),
        migrations.AddField(
            model_name='check',
            name='groupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.group'),
        ),
    ]
