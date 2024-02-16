from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length= 100, verbose_name = "Kategori İsmi")

  def __str__(self):
      return self.name

  class Meta:
     verbose_name_plural ="Kategoriler"
     verbose_name = "Kategori"

class SubCategory(models.Model):
   name = models.CharField(max_length = 100, verbose_name = "Kategori İsmi")
   def __str__(self):
       return self.name
   class Meta:
     verbose_name_plural ="Alt Kategoriler"
     verbose_name = "Alt Kategori"





class Product(models.Model):
  owner = models.ForeignKey(User, on_delete = models.CASCADE, null = True, verbose_name = "Satıcı")
  category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, verbose_name = "Kategori")
  sub_category = models.ManyToManyField(SubCategory)
  name = models.CharField(max_length = 100, verbose_name = "Ürün İsmi")
  content = RichTextField(verbose_name = "Açıklama")
  price = models.IntegerField(default = 0,verbose_name = "Fiyat")
  image = models.FileField(upload_to = "products/", null=True)
  favorites = models.ManyToManyField(User, verbose_name="Favoriye eklenenler", related_name="favorite_product")
  created_at = models.DateTimeField(auto_now_add = True, null=True, verbose_name="Oluşturulma Tarihi")
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural ="Ürünler"
    verbose_name = "Ürün"
  
class Cart(models.Model):
  buyer = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name ="Alıcı")
  product = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = "Eklenen Ürün")
  piece = models.IntegerField(default = 1, verbose_name = "Sepete eklenen adet")
  total_price = models.DecimalField(verbose_name = "Toplam Fiyat", editable = False, default = 0, max_digits = 50, decimal_places = 2)
  created_at = models.DateTimeField(auto_now_add = True)

  def __str__(self):
      return self.buyer.username
  class Meta:
     verbose_name_plural = "Sepetteki Ürünler"
     verbose_name = "Sepetteki Ürün"
  
  def save(self, *args, **kwargs):
     self.total_price = self.product.price * self.piece
     super().save(*args, **kwargs)