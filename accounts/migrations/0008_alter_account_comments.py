# Generated by Django 4.0.4 on 2022-05-20 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_account_profile_alter_account_sent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
