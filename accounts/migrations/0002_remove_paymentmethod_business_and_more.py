# Generated by Django 4.0.4 on 2022-05-18 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='business',
        ),
        migrations.AddField(
            model_name='accountname',
            name='perfil_quantity',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
