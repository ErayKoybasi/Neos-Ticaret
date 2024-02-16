from .models import *

def get_categories(request):
  categories = Category.objects.all()
  return {'categories': categories}

def get_count(request):
  sepetAdeti = Cart.objects.filter(buyer = request.user).count() if request.user.is_authenticated else 0
  return {'sepetAdeti':sepetAdeti}