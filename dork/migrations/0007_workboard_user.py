# Generated by Django 2.2.6 on 2020-02-09 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dork', '0006_auto_20200205_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='workboard',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workboards', to=settings.AUTH_USER_MODEL),
        ),
    ]
