# Generated by Django 5.0 on 2024-02-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ManyToManyField(to='products.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Kategori İsmi'),
        ),
    ]
