# Generated by Django 3.2 on 2021-08-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('movieId', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]
