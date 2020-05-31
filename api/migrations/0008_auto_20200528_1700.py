# Generated by Django 3.0.6 on 2020-05-28 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_parking_jours_d_ouverture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
