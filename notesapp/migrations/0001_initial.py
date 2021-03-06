# Generated by Django 3.1 on 2021-07-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'NEWEST'), ('old', 'OLDEST'), ('title', 'TITLE')], max_length=50)),
            ],
        ),
    ]
