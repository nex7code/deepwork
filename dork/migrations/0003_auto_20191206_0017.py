# Generated by Django 2.2.6 on 2019-12-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dork', '0002_subtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='backgroud_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='expected_total_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='real_total_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
