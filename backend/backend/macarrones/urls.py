from django.urls import path
from . import views

app_name = "macarrones"

urlpatterns = [
    path('', views.home, name="home"),
    path("macarrones/", views.macarrones_page, name="macarrones"),
    path("persona/<slug:slug>/", views.person_detail, name="person_detail"),
    path('products/', views.product_list_view, name='list'),
]
