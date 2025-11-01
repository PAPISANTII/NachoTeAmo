from django.shortcuts import render, get_object_or_404

from .models import Person
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import UploadProduct

# Create your views here.



def home(request):
    person_list = Person.objects.all()
    return render(request, "macarrones/home.html" , {'persons': person_list})

def macarrones_page(request):
    return render(request, "macarrones/macarrones.html")

def person_detail(request, slug):
    person = get_object_or_404(Person, slug=slug)
    return render(request, "macarrones/person_detail.html", {'person': person})

@login_required(login_url="/users/login/")
def product_list_view(request):
    product_list = Product.objects.all()[:20]
    
    if request.method =='POST' :
        form = UploadProduct(request.POST, request.FILES)
        if form.is_valid():
            newproduct = form.save(commit=False)
            newproduct.user = request.user
            newproduct.save()
            return redirect('macarrones:list')
    else:
        form = UploadProduct()
        
    return render(request, "macarrones/list.html", {'product_list': product_list, 'form': form})