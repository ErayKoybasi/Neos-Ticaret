# Generated by Django 5.0 on 2024-02-13 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_category_options_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Ürün', 'verbose_name_plural': 'Ürünler'},
        ),
        migrations.AddField(
            model_name='product',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_product', to=settings.AUTH_USER_MODEL, verbose_name='Favoriye eklenenler'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
    ]
