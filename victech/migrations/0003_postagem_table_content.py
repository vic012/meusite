# Generated by Django 4.1.1 on 2023-07-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("victech", "0002_postagem_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="postagem",
            name="table_content",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]