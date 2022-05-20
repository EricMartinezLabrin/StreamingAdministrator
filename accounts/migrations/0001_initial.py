# Generated by Django 4.0.4 on 2022-05-16 20:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('comments', models.CharField(blank=True, max_length=250, null=True)),
                ('profile', models.IntegerField()),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AccountName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=30)),
                ('headline', models.CharField(max_length=30)),
                ('card_number', models.CharField(max_length=16)),
                ('clabe', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('url', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('lada', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.business')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.business')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('lada', models.IntegerField()),
                ('country', models.CharField(max_length=40)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.business')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('payment_amount', models.IntegerField()),
                ('invoice', models.CharField(max_length=20)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.account')),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.bank')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.business')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer')),
                ('payment_method_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.paymentmethod')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.status')),
                ('user_seller_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bank',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.business'),
        ),
        migrations.AddField(
            model_name='account',
            name='account_name_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.accountname'),
        ),
        migrations.AddField(
            model_name='account',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.business'),
        ),
        migrations.AddField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='customer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer'),
        ),
        migrations.AddField(
            model_name='account',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.status'),
        ),
        migrations.AddField(
            model_name='account',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.supplier'),
        ),
    ]
