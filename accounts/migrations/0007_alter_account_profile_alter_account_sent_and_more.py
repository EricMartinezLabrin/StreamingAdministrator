# Generated by Django 4.0.4 on 2022-05-18 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_status_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='sent',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='status_id',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.status'),
        ),
    ]
