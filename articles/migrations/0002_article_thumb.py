# Generated by Django 4.2.4 on 2023-08-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="thumb",
            field=models.ImageField(blank=True, default="deafault.png", upload_to=""),
        ),
    ]
