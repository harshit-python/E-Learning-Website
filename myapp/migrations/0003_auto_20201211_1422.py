# Generated by Django 3.1.4 on 2020-12-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201211_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='mocktest',
            name='creator',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='mocktest',
            name='link',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='quiz',
            name='creator',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='quiz',
            name='link',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='link',
            field=models.CharField(default='', max_length=1000),
        ),
    ]