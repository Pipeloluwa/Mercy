# Generated by Django 3.2.13 on 2022-05-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ty', '0017_alter_book_maximum_no_of_borrowing_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=50),
        ),
    ]
