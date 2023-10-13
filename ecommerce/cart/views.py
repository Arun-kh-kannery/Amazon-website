from django.shortcuts import render,redirect
from shop.models import Product
from cart.models import Cart,Account,Order
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def addtocart(request,p):
    product=Product.objects.get(pname=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,product=product)
        if(cart.quantity<cart.product.stock):
            cart.quantity+=1
        cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(product=product,user=user,quantity=1)
        cart.save()
    # return render(request,'cart.html',{'cart':cart})
    return redirect('cart:cart_view')
@login_required
def cart_view(request):
    total=0
    user=request.user
    try:
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.product.price*i.quantity
    except:
        pass
    return render(request,'cart.html',{'cart':cart,'total':total})
@login_required
def cart_remove(request,p):
    product=Product.objects.get(pname=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,product=product)
        if(cart.quantity > 1):
            cart.quantity -=1
            cart.save()
        else:
            cart.delete()
    except:
        pass
    return redirect('cart:cart_view')
@login_required
def cart_full_remove(request,p):
    product=Product.objects.get(pname=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,product=product)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')
@login_required
def order(request):
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['ac']
        user=request.user
        cart=Cart.objects.filter(user=user)
        total=0
        for i in cart:
            total+=i.quantity*i.product.price
        acct=Account.objects.get(acctnumber=n)
        if(acct.balance >= total):
            acct.balance-=total
            acct.save()
            for i in cart:
                order=Order.objects.create(user=user,product=i.product,phone=p,address=a,no_of_items=i.quantity,order_status="paid")
                order.save()
                i.product.stock=i.product.stock-i.quantity
                i.product.save()
            cart.delete()
            msg="ORDER PLACED SUCCESSFULLY"
            return render(request,'orderconfirm.html',{'msg':msg})
        else:
            msg="Insufficient Balance.You Cant Place Order"
            return render(request,'orderconfirm.html',{'msg':msg})
    return render(request,'order.html')
@login_required
def orderview(request):
    user=request.user
    try:
        order=Order.objects.filter(user=user)
    except:
        pass
    return render(request,'orderview.html',{'order':order,'u':user.username})