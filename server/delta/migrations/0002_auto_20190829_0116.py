# Generated by Django 2.2.3 on 2019-08-28 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='function',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='status',
            new_name='led',
        ),
    ]
