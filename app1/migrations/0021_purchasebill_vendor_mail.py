# Generated by Django 4.1.7 on 2023-08-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_vendor_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasebill',
            name='vendor_mail',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
