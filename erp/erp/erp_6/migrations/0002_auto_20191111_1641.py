# Generated by Django 2.0.7 on 2019-11-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_6', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='button',
            field=models.CharField(default='补货申请', max_length=10),
        ),
    ]
