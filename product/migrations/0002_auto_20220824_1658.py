# Generated by Django 2.2 on 2022-08-24 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_merchant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="users.Merchant",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_package",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="product.Package",
            ),
        ),
        migrations.AddField(
            model_name="package",
            name="package_category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="packages",
                to="product.Category",
            ),
        ),
    ]