# Generated by Django 4.1.3 on 2022-11-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Transaction_id',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
