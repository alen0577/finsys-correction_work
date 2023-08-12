# Generated by Django 3.2.14 on 2023-05-25 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20230118_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetainerInvoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('billing_address', models.CharField(max_length=100, null=True)),
                ('invoice_date', models.DateField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('invoice_number', models.CharField(max_length=100, null=True)),
                ('reference_number', models.IntegerField(null=True)),
                ('place_of_supply', models.CharField(max_length=100, null=True)),
                ('total_amount', models.FloatField(max_length=100, null=True)),
                ('customer_notes', models.CharField(max_length=100, null=True)),
                ('terms_conditions', models.CharField(max_length=100, null=True)),
                ('comments', models.CharField(max_length=100, null=True)),
                ('attachment', models.ImageField(null=True, upload_to='retainer_invoices/')),
                ('status', models.CharField(max_length=100, null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='RetainerInvoiceItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('amount', models.FloatField(max_length=100, null=True)),
                ('retainer_invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.retainerinvoices')),
            ],
        ),
    ]
