# Generated by Django 2.0 on 2018-01-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20171231_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compute_resource_model',
            name='name',
            field=models.CharField(help_text='Test', max_length=10),
        ),
    ]
