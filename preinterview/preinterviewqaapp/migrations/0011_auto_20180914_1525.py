# Generated by Django 2.0 on 2018-09-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preinterviewqaapp', '0010_preinterviewmodel_interested_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preinterviewmodel',
            name='interested_job',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128),
        ),
    ]
