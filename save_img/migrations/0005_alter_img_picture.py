# Generated by Django 3.2.9 on 2021-11-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('save_img', '0004_alter_img_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]