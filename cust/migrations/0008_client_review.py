# Generated by Django 3.1.3 on 2020-11-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0007_auto_20201125_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='review',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]