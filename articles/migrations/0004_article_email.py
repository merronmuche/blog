# Generated by Django 4.1.3 on 2022-11-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='email',
            field=models.EmailField(default='mark@jkdjf.com', max_length=254),
        ),
    ]