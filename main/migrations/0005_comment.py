# Generated by Django 4.0.3 on 2022-07-27 17:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', tinymce.models.HTMLField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
