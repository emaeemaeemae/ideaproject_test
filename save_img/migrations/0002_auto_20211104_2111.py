# Generated by Django 3.2.9 on 2021-11-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('save_img', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='img',
            name='name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='img',
            name='parent_picture',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='img',
            name='picture',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='img',
            name='width',
            field=models.IntegerField(blank=True),
        ),
    ]
