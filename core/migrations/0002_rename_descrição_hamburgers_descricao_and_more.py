# Generated by Django 5.1.1 on 2024-09-14 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hamburgers',
            old_name='descrição',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='hamburgers',
            old_name='preço',
            new_name='preco',
        ),
        migrations.RenameField(
            model_name='sidedishes',
            old_name='descrição',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='sidedishes',
            old_name='preço',
            new_name='preco',
        ),
        migrations.RenameField(
            model_name='sweetstreats',
            old_name='descrição',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='sweetstreats',
            old_name='preço',
            new_name='preco',
        ),
    ]
