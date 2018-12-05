# Generated by Django 2.1.1 on 2018-12-01 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discourz_app', '0015_polltopic_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debates',
            name='category',
        ),
        migrations.RemoveField(
            model_name='pastdebates',
            name='category',
        ),
        migrations.RemoveField(
            model_name='polltopic',
            name='category',
        ),
        migrations.AddField(
            model_name='debates',
            name='tags',
            field=models.CharField(default='["General"]', max_length=100),
        ),
        migrations.AddField(
            model_name='pastdebates',
            name='tags',
            field=models.CharField(default='["General"]', max_length=100),
        ),
        migrations.AddField(
            model_name='polltopic',
            name='tags',
            field=models.TextField(default='["General"]', max_length=100),
        ),
    ]