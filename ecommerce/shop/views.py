from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def allproduct(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
def allproducts(request,c):
    p=Product.objects.filter(category__cname=c) #syntax
    category=Category.objects.get(cname=c)
    return render(request,'products.html',{'p':p,'category':category})
def productdetails(request,p):
    c=Product.objects.get(pname=p)
    return render(request,'details.html',{'p':c})
def userlogin(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect("shop:allcat")
        else:
            messages.error(request, "invalid credentials")
        return render(request, 'login.html')

    return render(request,'login.html')
def usersignup(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p= request.POST['p']
        p1 = request.POST['p1']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if(p==p1):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect("shop:allcat")

    return render(request,'signup.html')
def userlogout(request):
    logout(request)
    return redirect('shop:allcat')