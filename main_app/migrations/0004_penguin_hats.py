# Generated by Django 4.2.1 on 2023-06-03 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_hat_alter_feeding_options_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='penguin',
            name='hats',
            field=models.ManyToManyField(to='main_app.hat'),
        ),
    ]