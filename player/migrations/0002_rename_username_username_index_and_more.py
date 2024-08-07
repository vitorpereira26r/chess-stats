# Generated by Django 5.0.7 on 2024-08-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='playerrequests',
            new_name='username_index',
            old_name='username',
        ),
        migrations.AlterField(
            model_name='playerrequests',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
