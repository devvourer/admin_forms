# Generated by Django 3.2.4 on 2021-06-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generators', '0003_generator_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field',
            field=models.CharField(choices=[('text', 'text'), ('email', 'mail'), ('file', 'file')], max_length=30),
        ),
    ]
