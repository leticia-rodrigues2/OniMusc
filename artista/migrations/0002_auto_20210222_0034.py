# Generated by Django 3.1.7 on 2021-02-22 00:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_Post_Musc', models.DateField(auto_now_add=True)),
                ('duracao', models.PositiveIntegerField()),
                ('obesrvacoes', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='artista',
            name='dt_inicio',
        ),
        migrations.AddField(
            model_name='artista',
            name='data_inicio',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
