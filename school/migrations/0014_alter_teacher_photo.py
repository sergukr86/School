# Generated by Django 4.2.6 on 2023-10-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0013_teacher_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="photo",
            field=models.ImageField(height_field="70", upload_to="", width_field="50"),
        ),
    ]
