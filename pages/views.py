from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/home.html')


def product(request):
    return render(request,'pages/products.html',{'title':'Products'})

def contact(request):
    return render(request,'pages/contact.html',{'title':'Contact'})

def about(request):
    return render(request,'pages/about.html',{'title':'about'})