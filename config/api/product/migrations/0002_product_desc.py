# Generated by Django 4.1.3 on 2022-11-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
