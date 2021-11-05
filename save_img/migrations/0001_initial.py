# Generated by Django 3.2.9 on 2021-11-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=150)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('parent_picture', models.IntegerField()),
            ],
        ),
    ]