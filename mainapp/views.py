from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForm
from xhtml2pdf import pisa
# Create your views here.
from .models import Product,Order,Category,Carousel
from .cart import Cart
import string
import random
import uuid



def generate_unique_code():
    #length = 6

    while True:
        code = str(uuid.uuid1())
        code=code[:7]
        if Order.objects.filter(code=code).count() == 0:
            break

    return code

def home(request):
    covid19_care=Product.objects.filter(product_category=Category.objects.get(category_name='Covid-19 care'))
   
    coursel=Carousel.objects.get(id_image=1)
    coursel_2=Carousel.objects.get(id_image=2)
    return render(request,'index.html',context={'covid':covid19_care,'coursel':coursel,'coursel_2':coursel_2})

def _404_page(request,exception):
    return render(request,'page_404.html')

def add(request):
    '''if request.method=="POST":
        file=request.POST['file']
        o=Order(order_data=file,order_completed=True)
        o.save()
        return HttpResponse("success")'''
    form=OrderForm(request.POST)
    form.save()


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_decrement(request, id):
    if request.is_ajax():
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
        return redirect("cart_detail")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    print(request.POST)
    print(request.session.get('cart'))
    return render(request, 'cart.html')
    
def hf(request,category):
    p=Product.objects.filter(product_sub_category=category)
    return render(request,'hf.html',context={'f':p})
    


def addtobase(request):
    if request.method=='POST':
        if request.session.get('cart'):
            x=list(request.session.get('cart').keys())
            y=list(request.session.get('cart').values())
            print("Y:",y)
            print(x)
            for i in range(len(x)):
                print("i:",i)
                p=Product.objects.get(id=int(x[i]))
                quantity=y[i]
                o=Order(code=generate_unique_code(),product=p,product_quantity=quantity['quantity'],customer_name=request.POST['firstname'],customer_email=request.POST['email'],customer_number=request.POST['city'],customer_address=request.POST['address'],order_completed=False)
                o.save()
            return cart_clear(request)


def detail(request,id):
    product=Product.objects.get(id=id)
    print(product.product_customization)
    return render(request,'detail.html',context={'product':product})


def product_page(request,category):
    items=Product.objects.filter(product_sub_category__contains=category)
    return render(request,'products.html',{'items':items})
    

def search(request):
    if request.method=='GET':
        keyword=request.GET['search']
        items=Product.objects.filter(product_sub_category__contains=keyword)
        if len(items)>0:
            return render(request,'products.html',{'items':items})
        else:
            items=Product.objects.all()
            return render(request,'products.html',{'items':items,'notfound':'Oops! We couldn\'t process your request.  See our other products!'})