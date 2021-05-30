# Generated by Django 3.2.2 on 2021-05-15 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(),
        ),
    ]