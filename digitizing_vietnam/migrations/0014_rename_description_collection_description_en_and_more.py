# Generated by Django 4.2.13 on 2024-07-03 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitizing_vietnam', '0013_alter_onlineresourcecategory_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='onlineresource',
            old_name='category',
            new_name='category_en',
        ),
        migrations.RenameField(
            model_name='onlineresource',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='onlineresource',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='onlineresourcecategory',
            old_name='category_name',
            new_name='category_name_en',
        ),
        migrations.RenameField(
            model_name='onlineresourcecategory',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='information',
        ),
    ]
