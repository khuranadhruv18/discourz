# Generated by Django 2.1.1 on 2018-10-24 01:05

import discourz_app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='static/avatar/man1.png', upload_to=discourz_app.models.user_directory_path)),
                ('bio', models.TextField(default='tell us about yourself', max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PollTopic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular poll topic', primary_key=True, serialize=False)),
                ('title', models.TextField(default='', max_length=100)),
                ('options', models.TextField(default='', max_length=500)),
                ('votes', models.TextField(default='', max_length=500)),
                ('img', models.ImageField(default='static/avatar/man1.png', upload_to=discourz_app.models.poll_directory_path)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='discourz_app.Account')),
            ],
        ),
    ]
