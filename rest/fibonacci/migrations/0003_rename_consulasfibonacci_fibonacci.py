# Generated by Django 4.1 on 2022-08-19 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0002_alter_consulasfibonacci_total'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConsulasFibonacci',
            new_name='Fibonacci',
        ),
    ]
