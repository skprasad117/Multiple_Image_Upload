# Generated by Django 4.2.3 on 2023-07-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("multipleimagesapp", "0002_rename_image_gallery_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="title",
            field=models.CharField(blank=True, default="No Title", max_length=50),
        ),
    ]
