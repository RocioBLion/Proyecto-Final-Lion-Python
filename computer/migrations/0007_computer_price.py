# Generated by Django 4.1.3 on 2022-12-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0006_remove_computer_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
