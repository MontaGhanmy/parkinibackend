# Generated by Django 3.0.6 on 2020-06-23 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200619_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupation',
            name='date_debut',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
