# Generated by Django 4.0.4 on 2022-05-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile',
            field=models.IntegerField(default=1, null=True),
        ),
    ]