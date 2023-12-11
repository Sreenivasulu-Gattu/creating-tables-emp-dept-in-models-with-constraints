# Generated by Django 4.2.7 on 2023-12-11 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('deptno', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='salgrade',
            fields=[
                ('grade', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('losal', models.PositiveIntegerField()),
                ('hisal', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='emp',
            fields=[
                ('empno', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('mgr', models.PositiveIntegerField()),
                ('hiredate', models.DateField()),
                ('sal', models.PositiveIntegerField()),
                ('comm', models.PositiveIntegerField(null=True)),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]