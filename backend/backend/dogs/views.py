from django.shortcuts import render
import requests

# Create your views here.
def random_dog_view(request):
    url= "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    
    context = {
        'image_url': data.get('message'),
        'status': data.get('status'),
    }
    return render(request, 'dogs/random_dog.html', context)