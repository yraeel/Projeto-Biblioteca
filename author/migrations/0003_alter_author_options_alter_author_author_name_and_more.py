# Generated by Django 5.1.2 on 2024-11-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_id_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
    ]
