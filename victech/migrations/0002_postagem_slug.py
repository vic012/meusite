# Generated by Django 3.2.15 on 2022-11-11 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('victech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]