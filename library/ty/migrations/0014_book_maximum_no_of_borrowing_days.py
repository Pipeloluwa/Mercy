# Generated by Django 3.2.13 on 2022-05-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ty', '0013_book_return_and_history_book_cover_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='maximum_no_of_borrowing_days',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]
