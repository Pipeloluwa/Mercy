# Generated by Django 3.2.13 on 2022-05-11 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ty', '0021_book_return_and_history_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_return_and_history',
            name='no',
        ),
    ]
