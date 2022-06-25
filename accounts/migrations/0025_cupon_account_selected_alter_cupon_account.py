# Generated by Django 4.0.4 on 2022-06-23 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_cupon_sale_alter_cupon_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupon',
            name='account_selected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='cupon',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.accountname'),
        ),
    ]
