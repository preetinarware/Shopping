# Generated by Django 3.2.7 on 2021-09-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_oders_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('gender', models.CharField(max_length=15)),
                ('contact', models.IntegerField(max_length=10)),
                ('Current_add', models.TextField(max_length=50)),
                ('Permanant_add', models.TextField(max_length=50)),
                ('DOB', models.DateField()),
            ],
        ),
    ]
