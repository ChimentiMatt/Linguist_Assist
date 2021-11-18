# Generated by Django 3.2.9 on 2021-11-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellingapp', '0002_keyval_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyval',
            name='spelling_error',
            field=models.CharField(db_index=True, default='.', max_length=240),
        ),
        migrations.AlterField(
            model_name='keyval',
            name='word',
            field=models.CharField(db_index=True, default='.', max_length=240),
        ),
    ]
