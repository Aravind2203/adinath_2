# Generated by Django 3.1.4 on 2021-01-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_invitations'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]
