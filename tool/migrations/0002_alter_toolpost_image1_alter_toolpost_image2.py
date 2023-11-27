# Generated by Django 4.0 on 2023-11-20 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolpost',
            name='image1',
            field=models.ImageField(upload_to='tool_img', verbose_name='イメージ1'),
        ),
        migrations.AlterField(
            model_name='toolpost',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='tool_img', verbose_name='イメージ2'),
        ),
    ]