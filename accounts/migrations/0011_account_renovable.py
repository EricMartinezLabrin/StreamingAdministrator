# Generated by Django 4.0.4 on 2022-05-26 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_userdetail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='renovable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
