# Generated by Django 3.1.2 on 2020-10-22 01:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20201021_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Id unico de cada Marca', primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
            ],
        ),
    ]
