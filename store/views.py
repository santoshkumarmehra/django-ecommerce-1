from django.shortcuts import render, redirect
from .models import Product, Category, Customer, Order
from django.views import View
from django.contrib.auth.decorators import login_required


class Index(View):
    
    def post(self, request):
        if request.session.get('customer_id'):
            product = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity + 1
                else:
                    cart[product] = 1
            else: 
                cart = {}
                cart[product] = 1
            request.session['cart'] = cart
            return redirect('/home/')
        else:
            return redirect('/login/')


    def get(self, request):
        if request.session.get('customer_id'):
            cart = request.session.get('cart')
            if not cart:
                request.session['cart']={}
            categories = Category.get_all_category()
            categoryID = request.GET.get('category')
            if categoryID:
                product = Product.get_all_product_by_categoryid(categoryID)
            else:
                product = Product.get_all_product()
            data = {}
            data['products'] = product
            data['categories'] = categories
            return render(request, 'index.html', data)
        else:
            return redirect('/login/')


class Cart(View):
    def get(self, request):
        if request.session.get('customer_id'):
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            numberodcart = request.session.get('cart')            
            return render(request, 'cart.html', {'products':products})
        else:
            return redirect('/login/')


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phoneno = postData.get('phoneno')
        email = postData.get('email')
        password = postData.get('password')
        
        customer = Customer(
            first_name = first_name,
            last_name = last_name,
            phoneno = phoneno,
            email = email,
            password = password,
        )
        customer.register()
        return redirect('/login/')


def Login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        # customer = Customer.objects.filter(email=email)
        customer = Customer.get_customer_by_email(email)
        if customer:
            if customer.password ==password:
                request.session['customer_id'] = customer.id                
                return redirect('/home/')
            else:
                error_msg='Email or Password is invalid !!!'
                return render(request, 'login.html', {'error_msg':error_msg})
        elif customer == False:
            error_msg='Email or Password is invalid !!!'
            return render(request, 'login.html', {'error_msg':error_msg})


def Logout(request):
    request.session.clear()
    return redirect('/login/')


def checkout(request):
    if request.session.get('customer_id'):
        if request.method == "GET":
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            numberodcart = request.session.get('cart')            
            return render(request, 'checkout.html', {'products':products})
    else:
        return redirect('/login/')
    

def payment(request,id):
    if request.session.get('customer_id'):
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        for product in products:
            Order.objects.create(customer = Customer(id=customer),
                                product = product,
                                price = product.price,
                                quantity = cart.get(str(product.id)),
                                Transaction_id = id
            )
        request.session['cart'] = {}
        return redirect('/')
    else:
        return redirect('/login/')





   