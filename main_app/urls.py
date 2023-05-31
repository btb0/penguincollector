from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('penguins/', views.penguins_index, name='penguins_index'),
    path('penguins/<int:penguin_id>/', views.penguins_detail, name='penguins_detail'),
]