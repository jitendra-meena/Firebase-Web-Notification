# Generated by Django 3.2.13 on 2022-04-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('dob', models.DateField(default=0, max_length=8)),
                ('gender', models.CharField(blank=True, max_length=30)),
                ('county', models.CharField(blank=True, max_length=20)),
                ('code_info', models.CharField(max_length=70)),
            ],
        ),
    ]