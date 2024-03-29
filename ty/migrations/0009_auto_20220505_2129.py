# Generated by Django 3.2.13 on 2022-05-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ty', '0008_alter_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='test', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='privatize_book',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
