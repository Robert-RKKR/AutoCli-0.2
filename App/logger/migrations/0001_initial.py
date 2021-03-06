# Generated by Django 3.2.7 on 2021-10-12 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoggerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('process', models.IntegerField()),
                ('application', models.CharField(max_length=128)),
                ('module', models.CharField(max_length=128, null=True)),
                ('severity', models.IntegerField(choices=[(1, 'DEBUG'), (2, 'INFO'), (3, 'WARNING'), (4, 'ERROR'), (5, 'CRITICAL')])),
                ('message', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
                ('logger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logger.loggerdata')),
            ],
        ),
    ]
