# Generated by Django 4.2 on 2024-06-26 21:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_category_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Category"},
        ),
        migrations.RenameField(
            model_name="product",
            old_name="Category",
            new_name="category",
        ),
    ]
