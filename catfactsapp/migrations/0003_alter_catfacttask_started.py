# Generated by Django 4.2.16 on 2024-09-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catfactsapp', '0002_alter_catfacttask_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catfacttask',
            name='started',
            field=models.DateTimeField(null=True),
        ),
    ]
