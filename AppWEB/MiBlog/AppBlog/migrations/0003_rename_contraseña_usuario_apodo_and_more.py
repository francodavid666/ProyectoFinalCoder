# Generated by Django 4.1 on 2022-09-23 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_alter_usuario_contraseña'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='apodo',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='email',
            new_name='codigo_postal',
        ),
    ]
