# Generated by Django 2.2.6 on 2020-06-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=512)),
            ],
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
