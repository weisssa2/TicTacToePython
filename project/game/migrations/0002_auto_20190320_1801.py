# Generated by Django 2.1.7 on 2019-03-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]