# Generated by Django 5.1.1 on 2024-11-05 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stars',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_venc',
            field=models.DateField(null=True),
        ),
    ]
