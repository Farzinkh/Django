# Generated by Django 2.2.3 on 2019-09-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0003_auto_20190907_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='moisture',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
