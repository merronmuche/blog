# Generated by Django 4.1.3 on 2022-11-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_articles_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
    ]
