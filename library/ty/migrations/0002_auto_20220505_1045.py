# Generated by Django 3.2.13 on 2022-05-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover_picture',
            field=models.ImageField(default='test', upload_to='bookcover'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_return_and_history',
            name='author',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_return_and_history',
            name='title',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]