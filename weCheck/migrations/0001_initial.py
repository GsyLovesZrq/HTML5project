# Generated by Django 2.0.7 on 2018-08-13 11:43

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
                ('duration', models.IntegerField(max_length=5)),
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
                ('duration', models.IntegerField(max_length=5)),
                ('repeat', models.CharField(max_length=20)),
                ('enable', models.BooleanField(default=False)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupID', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('member', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('passwd', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=10)),
                ('profile', models.CharField(max_length=100)),
                ('userType', models.IntegerField(max_length=1)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='userToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=32)),
                ('domain', models.CharField(max_length=30)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.user', to_field='username')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.user', to_field='username'),
        ),
        migrations.AddField(
            model_name='checkplan',
            name='groupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.group', to_field='groupID'),
        ),
        migrations.AddField(
            model_name='check',
            name='groupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.group', to_field='groupID'),
        ),
    ]
