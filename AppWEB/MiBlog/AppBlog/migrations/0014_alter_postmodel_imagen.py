# Generated by Django 4.1 on 2022-10-20 04:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0013_alter_postmodel_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='imagen',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
