from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import RegisterForm, ProductForm
from .models import Product, Cart, CartItem

def home(request):
    products = Product.objects.select_related('owner').prefetch_related('categories').all()
    return render(request, 'store/home.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    if not request.user.is_seller:
        return HttpResponseForbidden("No tienes permisos")
    products = Product.objects.filter(owner=request.user)
    return render(request, 'store/dashboard.html', {'products': products})

@login_required
def product_create(request):
    if not request.user.is_seller:
        return HttpResponseForbidden("Solo vendedores")
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.owner = request.user
        product.save()
        form.save_m2m()
        return redirect('dashboard')
    return render(request, 'store/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.owner != request.user:
        return HttpResponseForbidden("No puedes editar este producto")
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'store/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.owner != request.user:
        return HttpResponseForbidden("No puedes eliminar este producto")
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(request, 'store/product_confirm_delete.html', {'product': product})

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart_detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    
    if product.stock <= 0:
        messages.error(request, f"No hay stock de {product.name}")
        return redirect('cart_detail')
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        if cart_item.quantity + 1 > product.stock:
            messages.error(request, f"No hay suficiente stock. Solo hay {product.stock}")
            return redirect('cart_detail')
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"Se agregó otra unidad de {product.name}")
    else:
        messages.success(request, f"{product.name} agregado al carrito")
    
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = item.product.name
    item.delete()
    messages.success(request, f"{product_name} eliminado del carrito")
    return redirect('cart_detail')

@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        
        if quantity > 0:
            if quantity > item.product.stock:
                messages.error(request, f"No hay suficiente stock. Solo hay {item.product.stock}")
                return redirect('cart_detail')
            item.quantity = quantity
            item.save()
            messages.success(request, f"Cantidad actualizada a {quantity}")
        else:
            item.delete()
            messages.success(request, f"{item.product.name} eliminado del carrito")
    
    return redirect('cart_detail')