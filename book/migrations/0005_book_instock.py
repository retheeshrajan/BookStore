# Generated by Django 2.1.7 on 2019-02-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20190213_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='inStock',
            field=models.BooleanField(default=True),
        ),
    ]