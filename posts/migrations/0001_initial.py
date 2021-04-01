# Generated by Django 3.1.7 on 2021-03-26 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=120)),
                ('testo', models.TextField()),
                ('hash', models.CharField(blank=True, max_length=32, null=True)),
                ('txId', models.CharField(blank=True, default='Invio transazione in corso...', max_length=66, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_pubblicazione', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
