# Generated by Django 2.2.10 on 2021-05-05 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_auto_20210505_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollmodel',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
