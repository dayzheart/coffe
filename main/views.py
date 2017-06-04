from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import datetime
from django.core.mail import send_mail
from .forms import *

from django.conf import settings

# Create your views here.




def home(request):
    context = {}
    user = request.user
    context['user']=user
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            context['form']=form
            date = form.cleaned_data['data']
            context['today']=date
            order_list = order.objects.filter(user)
            context['order_list']=order_list
        else:
            form=  SearchForm()
            context['form']=form
            today = datetime.date,today()
            context[b

    return render(request, 'home.html', ())
def createcoffe(request):
    context={}
    if request.method == 'POST':
        form =CoffeForm(request.POST)

        if form_is_valid():
            coffee=form.save(comit=False)
            coffee.user = request.User
            coffee.save()
            return redirect("home")
        else:
            return render(request, 'createcoffe.html', context)
    else:
            form = CoffeForm()
            context['form']=form
            return render(request, 'createcoffe.html', context)





def editcoffe(request, coffe_id):
    contex={}
    coffee = Coffe.objects.get(id=coffee_id)
    context["coffee"]=coffee
    if request.method == 'POST':
        form =CoffeForm(instance=coffee)
        context['form']=form
        if form_is_valid():
            coffee=form.save(comit=False)
            coffee.user = request.user
            coffee.save_m2m()
            return redirect("home")
        else:
            return render(request, 'editcoffe.html', context)
    else:
            form = CoffeForm(instance=coffee)
            context['form']=form
            return render(request, 'editcoffe.html', context)

def createBean(request):
    context = {}
    if request.method == "POST":
        form = BeanForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createBean.html', context)
    else:
        form = BeanForm()
        context['form']=form
        return render(request, 'createBean.html', context)

def editBean(request, bean_id):
    context = {}
    bean = Bean.objects.get(id=bean_id)
    context['bean']=bean
    if request.method == "POST":
        form = BeanForm(request.POST,instance=bean)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editBean.html', context)
    else:
        form = BeanForm(instance=bean)
        context['form']=form
        return render(request, 'editBean.html', context)

def deleteBean(request, bean_id):
    Bean.objects.get(id=bean_id).delete()
    return redirect("home")



def createRoast(request):
    context = {}
    if request.method == "POST":
        form = RoastForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createRoast.html', context)
    else:
        form = RoastForm()
        context['form']=form
        return render(request, 'createRoast.html', context)

def editRoast(request, roast_id):
    context = {}
    roast = Roast.objects.get(id=roast_id)
    context['roast']=roast
    if request.method == "POST":
        form = RoastForm(request.POST,instance=roast)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editRoast.html', context)
    else:
        form = RoastForm(instance=roast)
        context['form']=form
        return render(request, 'editRoast.html', context)

def deleteRoast(request, roast_id):
    Roast.objects.get(id=roast_id).delete()
    return redirect("home")

def createSyrup(request):
    context = {}
    if request.method == "POST":
        form = SyrupForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createSyrup.html', context)
    else:
        form = SyrupForm()
        context['form']=form
        return render(request, 'createSyrup.html', context)

def editSyrup(request, syrup_id):
    context = {}
    syrup = Syrup.objects.get(id=syrup_id)
    context['syrup']=syrup
    if request.method == "POST":
        form = SyrupForm(request.POST,instance=syrup)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editSyrup.html', context)
    else:
        form = SyrupForm(instance=syrup)
        context['form']=form
        return render(request, 'editSyrup.html', context)

def deleteSyrup(request, syrup_id):
    Syrup.objects.get(id=syrup_id).delete()
    return redirect("home")


def createPowder(request):
    context = {}
    if request.method == "POST":
        form = PowderForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createPowder.html', context)
    else:
        form = PowderForm()
        context['form']=form
        return render(request, 'createPowder.html', context)

def editPowder(request, powder_id):
    context = {}
    powder = Powder.objects.get(id=powder_id)
    context['powder']=powder
    if request.method == "POST":
        form = PowderForm(request.POST,instance=powder)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editPowder.html', context)
    else:
        form = PowderForm(instance=powder)
        context['form']=form
        return render(request, 'editPowder.html', context)

def deletePowder(request, powder_id):
    Powder.objects.get(id=powder_id).delete()
    return redirect("home")


def createOrder(request, coffee_id):
    context = {}
    coffee = Coffee.objects.get(id=coffee_id)
    context['coffee']=coffee
    if request.method == "POST":
        form = OrderForm(request.POST)
        context['form']=form
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.coffee = coffee
            order.save()
            return redirect("home")
        else:
            return render(request, 'createOrder.html', context)

    else:
        form = OrderForm()
        context['form']=form
        return render(request, 'createOrder.html', context)

def user_list(request):
    context = {}
    user_list = User.objects.all()
    context['user_list'] = user_list
    return render(request, 'user_list.html', context)

def user_coffees(request, user_id):
    context = {}
    user = User.objects.get(id=user_id)
    context['user'] = user
    coffees = Coffee.objects.filter(user=user)
    context['coffees'] = coffees
    return render(request, 'user_coffees.html', context)



def send_order_email(request, date):
    context ={}
    date = datetime.datetime.strptime('%s%s%s'%(year month, day), "%Y%m%d").date()
    order_list = order.objects.filter(user=request.user, date = date)
    subject= "HAHHHAHAH SPAAAAAM I OWN YOU ! YOU ARE A NOOB !"
    subject2 = "Coded coffee reequest"
    message ="These are my orders, make yourself useful and get thme : \n"

    for order in order_list:
        message += "%s, " %(order.coffee)
        message2 =" hi "
    for order in oorder_list:
            message2 += "%s,"%(order.coffee.name)
    send_mail(subject, message,settings.EMAIL_HOST_USER, ['alsaff1987@gmail.com','sc.sara.hasan@gmail.com',] )
    send_mail(subject, message,settings.EMAIL_HOST_USER, ['hashim@joincoded.com','sc.sara.hasan@gmail.com',] )

    return redirect("home")
