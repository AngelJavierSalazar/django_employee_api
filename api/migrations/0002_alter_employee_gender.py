# Generated by Django 4.0.6 on 2022-07-12 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='gender'),
        ),
    ]
