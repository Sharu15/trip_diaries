# Generated by Django 2.1.2 on 2018-10-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
