# Generated by Django 3.2.7 on 2021-09-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=15)),
                ('h1', models.TextField(max_length=30)),
                ('h2', models.TextField(max_length=30)),
            ],
        ),
    ]
