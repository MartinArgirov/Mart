# Generated by Django 4.1.1 on 2022-10-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=10)),
                ('categoria', models.CharField(max_length=30)),
                ('mes', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
    ]
