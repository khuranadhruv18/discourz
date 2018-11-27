# Generated by Django 2.1.1 on 2018-11-27 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discourz_app', '0007_auto_20181106_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='myusername', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='debates',
            name='position',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pastdebates',
            name='user1Position',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pastdebates',
            name='user2Position',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='votedusers',
            name='debateVoted',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discourz_app.PastDebates'),
        ),
    ]