from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse

from django.contrib import messages
from .models import ProductImag, Product, Profile,CartProduct,Cart
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,ProfileForm,UserForm
from .serializers import PostSerializer
from rest_framework import viewsets
from django.utils import timezone


#from django.template import loader
#from django.contrib.auth.forms import UserCreationForme

# Create your views here


def product_List(request):
    page_obj=Product.objects.all()
    paginator=Paginator(page_obj,4)
    page_number=request.GET.get('page')
    product=paginator.get_page(page_number)
    context={'product':product}
    return render(request,'ecommerce/index.html',context)



def product_ditele(request,id):
      Product_ditle=Product.objects.get(id=id)
      product=Product.objects.all()
      context={'Product_ditle':Product_ditle,'product':product}
      return render(request,'ecommerce\single_product.html',context)



def search(request):
    if request.method=='GET':

      srch=request.GET['Search']
    if srch !=None :
      product=Product.objects.all().filter(proName=srch)
      context={'productserch':product}

    return render(request,'ecommerce\search.html',context)


def singup(request):

        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user= form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            form = SignUpForm()
            return render(request,'ecommerce\signup.html',{'form': form })



@login_required(login_url='/accounts/login/')
def ShowProfile(request,slug=None):
         cp=CartProduct.objects.all().filter(user=request.user)
         if(slug==None):
            current_user = request.user
            slug=current_user.profile.slug
            profile=get_object_or_404(Profile,slug=slug)
            context={'profile': profile,'cp':cp}
            return render(request,'ecommerce\profile.html',context)
         profile=get_object_or_404(Profile,slug=slug)
         context={'profile': profile,'cp':cp}

         return render(request,'ecommerce\profile.html',context)




@login_required(login_url='/accounts/login/')
def ge_edtProfle(request):
     if request.method=='POST':
         user_from=UserForm(request.POST,instance=request.user)
         profile_form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
         if user_from.is_valid() and profile_form.is_valid():
             user_from.save()
             profile_form.save()
             slug=profile_form.cleaned_data.get("slug")
             pro=Profile.objects.all().filter(slug=slug)
             profile=None
             for i in pro:
                 profile=i.slug

             messages.success(request,'تم تعديل البيانات بنجاح')
             return redirect('http://127.0.0.1:8000/ecommerce/profile/',profile=profile)
     else:
         user_from=UserForm(instance=request.user)
         profile_form=ProfileForm(request.FILES,instance=request.user.profile)


     context={'user_from':user_from,'profile_form':profile_form}
     return render(request,'ecommerce\profile_updet.html',context)



@login_required(login_url='/accounts/login/')
def get_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
             messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    context={'form':form}
    return render(request,'ecommerce\change_password.html',context)









def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



'''@login_required(login_url='/accounts/login/')
def getCart(requset,id):
    product=Product.objects.get(id=id)
    ip=get_client_ip(requset)
    cart=Cart.objects.all().filter(C_ip=ip,C_Product=product.pk )
    proname=[]
    if  cart:
      cart=Cart.objects.all()
      for i in cart:
       product=Product.objects.get(id=i.C_Product)
       proname.append(proname)
       context={'cart':cart,'product':proname}
    else:
      cart=Cart()
      cart.C_Product=product.pk
      cart.C_ip=ip
      cart.C_category=product.proCategory
      cart.save()
      cart=Cart.objects.all()
      for i in cart:
       product=Product.objects.get(id=i.C_Product)
       proname.append(proname)
       context={'cart':cart,'product':product}
    return render(requset,'ecommerce\cart.html',context)'''



@login_required(login_url='/accounts/login/')

def add_to_cart(requset,slug):
    ip=get_client_ip(requset)
    product=get_object_or_404(Product,slug=slug)
    cart_prodct=CartProduct.objects.create(C_Product=product,user=requset.user, CP_isorder=False,C_ip=ip)
    cart_qs=Cart.objects.filter(user=requset.user,C_isorder=False)
    if cart_qs:
        order=cart_qs[0]
        if order.C_Products.filter(C_Product=product):
          cart_prodct.C_Quantity+=1
          cart_prodct.save()
        else:
            order.C_Products.add(cart_prodct)
    else:
        order_date=timezone.now()
        order=Cart.objects.create(user=requset.user, C_order_date= order_date)
        order.C_Products.add(cart_prodct)
        order.save()
    cp=CartProduct.objects.all()
    context={'cart':order,'cart_prodct':cp}
    return (render(requset,'ecommerce\cart.html',context))


def remove_to_cart(requset,slug):
    ip=get_client_ip(requset)
    product=get_object_or_404(Product,slug=slug)
    cart_qs=Cart.objects.filter(user=requset.user,C_isorder=False)
    if cart_qs:
        order=cart_qs[0]
        if order.C_Products.filter(C_Product=product):
            cart_prodct=CartProduct.objects.filter(C_Product=product,user=requset.user, CP_isorder=False,C_ip=ip)[0]
            #order.C_Products.remove(cart_prodct)
            cart_prodct.delete()
        else:
            redirect('http://127.0.0.1:8000/ecommerce/cart',slug=slug)
    else:
        redirect('http://127.0.0.1:8000/ecommerce/cart',slug=slug)
    cp=CartProduct.objects.all()
    context={'cart':order,'cart_prodct':cp}
    return (render(requset,'ecommerce\cart.html',context))






class Proapi(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class =PostSerializer




class pagination(ListView):
      model = ProductImag
      template_name="ecommerce/index.html"
      #paginate_by=3





