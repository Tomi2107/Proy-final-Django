# Generated by Django 4.1 on 2022-11-26 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_merge_20220513_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
