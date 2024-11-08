# Generated by Django 5.1.2 on 2024-11-08 22:44

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0003_alter_author_options_alter_author_author_name_and_more'),
        ('publisher', '0002_remove_publisher_author_publisher_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('book_name', models.CharField(max_length=254)),
                ('pages', models.IntegerField()),
                ('edition', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('release', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('fk_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='author.author')),
                ('fk_publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='publisher.publisher')),
            ],
            options={
                'db_table': 'books',
                'managed': True,
            },
        ),
    ]