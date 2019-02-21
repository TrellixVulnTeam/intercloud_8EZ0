# Generated by Django 2.0.10 on 2019-02-08 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200, null=True)),
                ('address', models.TextField(null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('school', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200, null=True)),
                ('course', models.CharField(max_length=200, null=True)),
                ('university_start', models.DateTimeField(null=True)),
                ('university_end', models.DateTimeField(null=True)),
                ('employment_status', models.CharField(max_length=20, null=True)),
                ('parent_employment', models.CharField(max_length=20, null=True)),
                ('prog_knowledge', models.CharField(max_length=20, null=True)),
                ('database_knowledge', models.CharField(max_length=20, null=True)),
                ('operatingsystem_knowledge', models.CharField(max_length=20, null=True)),
                ('othercomputing_courses', models.CharField(max_length=20, null=True)),
                ('benefitof_prog', models.CharField(max_length=20, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_student', models.BooleanField(default=False)),
            ],
        ),
    ]