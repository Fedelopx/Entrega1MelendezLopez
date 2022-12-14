# Generated by Django 4.0.6 on 2022-08-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=100)),
                ('pulgadas', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
