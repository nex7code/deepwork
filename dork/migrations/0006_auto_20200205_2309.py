# Generated by Django 2.2.6 on 2020-02-05 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ("dork", "0005_auto_20191209_0001"),
    ]

    operations = [
        migrations.RenameModel(old_name="Project", new_name="WorkBoard",),
        migrations.RenameField(
            model_name="task", old_name="project", new_name="workboard",
        ),
        migrations.AlterField(
            model_name="subtask",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dork.Task"
            ),
        ),
    ]
