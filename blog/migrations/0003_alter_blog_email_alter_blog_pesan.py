# Generated by Django 4.1.4 on 2023-01-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_title_blog_nama_rename_category_blog_pesan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Pesan',
            field=models.TextField(),
        ),
    ]