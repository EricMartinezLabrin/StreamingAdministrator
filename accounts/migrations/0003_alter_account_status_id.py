# Generated by Django 4.0.4 on 2022-05-18 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_paymentmethod_business_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='status_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.status'),
        ),
    ]
