# Generated by Django 4.2.6 on 2023-10-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0012_alter_student_admission_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="photo",
            field=models.ImageField(
                default="Null", height_field=70, upload_to="", width_field=50
            ),
            preserve_default=False,
        ),
    ]
