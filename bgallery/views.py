from django.shortcuts import render,redirect
from .form import ImageFormm
from .models import Imagee



# Create your views here.
def Index(request):
    
    if request.method == "POST":
        form=ImageFormm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            objj=form.instance
            return render(request,"sucess.html",{"objj":objj})  
    else:
        form=ImageFormm()    
    imgg=Imagee.objects.all()
    return render(request,"main.html",{"imgg":imgg,"form":form})


def Viewimagea(request):
    #data = Imagee.objects.all().order_by('-caption')
    data = Imagee.objects.order_by("category")
    kkk =data.filter(category='a')
    return render(request , "a.html" , {"jj":kkk})


def Viewimageb(request):
    data = Imagee.objects.order_by("category")
    ppp =data.filter(category='b')
    return render(request , "b.html" , {"jjj":ppp}) 

def Viewimagec(request):
    data = Imagee.objects.order_by("category")
    pp =data.filter(category='c')
    return render(request , "c.html" , {"jll":pp})     


def Notfilter(request):
    imgg=Imagee.objects.order_by("-image")
    return render(request,"gallery.html",{"imgg":imgg})


def Indexu(request):
    
    if request.method == "POST":
        form=ImageFormm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            objj=form.instance
            return render(request,"sucess.html",{"objj":objj})  
    else:
        form=ImageFormm()    
    imgg=Imagee.objects.all()
    return render(request,"main.html",{"imgg":imgg,"form":form})