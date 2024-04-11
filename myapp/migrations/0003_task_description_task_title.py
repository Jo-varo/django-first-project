# Generated by Django 5.0.4 on 2024-04-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
