# Generated by Django 4.1.1 on 2022-10-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_messages_delete_ingridient_alter_recipe_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='messages',
            field=models.TextField(),
        ),
    ]
