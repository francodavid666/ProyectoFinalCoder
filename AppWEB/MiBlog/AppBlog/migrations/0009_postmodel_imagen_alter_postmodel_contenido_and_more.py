# Generated by Django 4.1 on 2022-09-25 06:35

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0008_postmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='imagen',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='contenido',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
