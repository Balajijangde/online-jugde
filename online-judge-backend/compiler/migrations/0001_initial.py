# Generated by Django 4.0.4 on 2022-06-01 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=500)),
                ('createdOn', models.DateTimeField(verbose_name='created on')),
                ('testcase1', models.CharField(max_length=500)),
                ('testcase2', models.CharField(max_length=500)),
                ('testcase3', models.CharField(max_length=500)),
                ('answer1', models.CharField(max_length=100)),
                ('answer2', models.CharField(max_length=100)),
                ('answer3', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('registeredOn', models.DateTimeField(verbose_name='date registered')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verdict', models.CharField(max_length=10)),
                ('submittedOn', models.DateTimeField(verbose_name='time submitted')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compiler.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compiler.user')),
            ],
        ),
    ]
