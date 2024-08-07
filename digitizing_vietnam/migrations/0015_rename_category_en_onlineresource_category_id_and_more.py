# Generated by Django 4.2.13 on 2024-07-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitizing_vietnam', '0014_rename_description_collection_description_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlineresource',
            old_name='category_en',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='onlineresource',
            old_name='title_en',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='onlineresourcecategory',
            old_name='category_name_en',
            new_name='category_id',
        ),
        migrations.AddField(
            model_name='collection',
            name='description_vi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='title_vi',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='description_vi',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='title_vi',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
