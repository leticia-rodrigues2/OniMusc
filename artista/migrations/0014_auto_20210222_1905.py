# Generated by Django 3.1.7 on 2021-02-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0013_auto_20210222_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='data_Post_Musc',
            field=models.DateTimeField(),
        ),
    ]