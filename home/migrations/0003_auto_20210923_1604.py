# Generated by Django 3.2.7 on 2021-09-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='more_products',
            name='field_names',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='more_products',
            name='head1',
            field=models.TextField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='more_products',
            name='head2',
            field=models.TextField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
