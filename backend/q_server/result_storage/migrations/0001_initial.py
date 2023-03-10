# Generated by Django 4.1.7 on 2023-02-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField()),
                ('percent', models.FloatField()),
                ('in_candle', models.FloatField()),
                ('settings', models.CharField(max_length=300)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('percent',),
            },
        ),
    ]
