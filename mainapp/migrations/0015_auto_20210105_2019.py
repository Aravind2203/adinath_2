# Generated by Django 3.1.4 on 2021-01-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20210103_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='id',
        ),
        migrations.AddField(
            model_name='carousel',
            name='id_image',
            field=models.PositiveIntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
