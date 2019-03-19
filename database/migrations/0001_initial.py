# Generated by Django 2.1.5 on 2019-03-19 05:13

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
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=16)),
                ('customer_street', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=255)),
                ('customer_city', models.CharField(max_length=255)),
                ('customer_zip_code', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(11)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=16)),
                ('to_state', models.CharField(max_length=255)),
                ('to_city', models.CharField(max_length=255)),
                ('to_zip_code', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(11)])),
                ('address', models.CharField(max_length=255)),
                ('cost', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=16)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.CharField(max_length=255)),
            ],
        ),
    ]
