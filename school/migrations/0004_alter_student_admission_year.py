# Generated by Django 4.2.6 on 2023-10-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0003_subject_score_subject_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="admission_year",
            field=models.IntegerField(max_length=4),
        ),
    ]
