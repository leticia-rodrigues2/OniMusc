# Generated by Django 3.1.7 on 2021-02-22 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0011_auto_20210222_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='data_Post_Musc',
            field=models.DateField(),
        ),
    ]
