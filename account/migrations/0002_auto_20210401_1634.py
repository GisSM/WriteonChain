# Generated by Django 3.1.7 on 2021-04-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_ip',
            name='ip_utente',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
