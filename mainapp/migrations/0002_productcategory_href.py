# Generated by Django 3.2.5 on 2021-07-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='href',
            field=models.CharField(default='#', max_length=64, unique=True, verbose_name='ссылка'),
        ),
    ]
