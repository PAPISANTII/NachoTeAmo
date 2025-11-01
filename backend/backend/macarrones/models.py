from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    slug = models.SlugField(unique = True, blank=True)
    propic = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True)
    
    def __str__(self):
        return self.name
    
class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.city} ({self.person.name})"
    
CASAS = [
    ('TEC', 'Tecnologia'),
    ('MOD', 'Moda'),
    ('HOG', 'Hogar'),
    ('OTR', 'Otros'),
]
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=3, choices=CASAS)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}, by {self.user}"