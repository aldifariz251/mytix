# Generated by Django 4.0.6 on 2022-08-20 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_book_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]