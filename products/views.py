from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def index(request):
  products = Product.objects.all()
  if request.GET.get('query'):
    search = request.GET.get('query')
    products = Product.objects.filter(
      Q(name__icontains = search) | 
      Q(category__name__icontains = search)
    )
  #Favori ekleme...
  if 'fav' in request.POST:
    productId = request.POST.get('productId') 
    product = Product.objects.get(id = productId)
    if request.user.is_authenticated:
      if request.user in product.favorites.all():
        product.favorites.remove(request.user)
        product.save()
        messages.success(request,'Ürün favorilerden çıkarıldı.')
      else:
        product.favorites.add(request.user)
        product.save()
        messages.success(request,'Ürün favorilere eklendi')
      return redirect('index')  
    else:
      messages.error(request,'Favoriye eklemek için giriş yapmanız lazım.')

  #Sepete ekleme
  if 'cart' in request.POST:
    if request.user.is_authenticated:
      productId = request.POST.get('productId')
      product = Product.objects.get(id = productId)
      pieces = request.POST.get('pieces')
      if Cart.objects.filter(buyer = request.user, product = product).exists():
        myCart = Cart.objects.get(buyer = request.user, product = product)
        myCart.piece += int(pieces)
        myCart.save()
        messages.success(request, "Sepetiniz Güncellendi.")
        return redirect('index')
      else:
        newCart = Cart.objects.create(
          buyer = request.user,
          product = product,
          piece = int(pieces),
        )
        newCart.save()
        messages.success(request, '')
        return redirect('index')
    else:
      messages.error(request,'sepete ekleyebilmeniz için giriş yapmanız gerekiyor.')
  context = {
    'products': products,
  }
  return render(request, 'index.html',context)


def detail(request, productId):
  product = Product.objects.get(id=productId)
  context = {
    'product' : product
  }
  return render(request, 'detail.html', context)

@login_required(login_url = "/login/")

def create(request):
  form = ProductForm()
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      newProduct = form.save(commit = False)
      newProduct.owner = request.user
      newProduct.save()
      messages.success(request, 'Ürün başarılı bir şekilde oluşturuldu.')
      return redirect('index')
  context = {
      'form':form
  }
  return render(request, 'create.html', context)

@login_required(login_url = "login")
def cart(request):
  sepetim = Cart.objects.filter(buyer = request.user)
  if 'remove' in request.POST:
    sepetId = request.POST.get('sepetId')
    sepet = Cart.objects.get(id=sepetId)
    sepet.delete()
    messages.success(request, 'ürün sepetten çıkarıldı')
    return redirect('cart')
  if 'update' in request.POST:
    sepetId = request.POST.get('sepetId')
    sepet = Cart.objects.get(id=sepetId)
    yeniAdet = int(request.POST.get('yeniAdet'))
    sepet.piece = yeniAdet
    sepet.save()
    messages.success(request, f'{sepet} Ürünün adeti {yeniAdet} olarak güncellendi.')

  context = {
    'sepetim':sepetim
  }
  return render(request, 'cart.html', context)