from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('penguins/', views.penguins_index, name='penguins_index'),
    path('penguins/<int:penguin_id>/', views.penguins_detail, name='penguins_detail'),
    path('penguins/create/', views.PenguinCreate.as_view(), name='penguins_create'),
    path('penguins/<int:pk>/update/', views.PenguinUpdate.as_view(), name='penguins_update'),
    path('penguins/<int:pk>/delete/', views.PenguinDelete.as_view(), name='penguins_delete'),
    path('penguins/<int:penguin_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('penguins/<int:penguin_id>/add_photo/', views.add_photo, name='add_photo'),
    path('penguins/<int:penguin_id>/assoc_hat/<int:hat_id>/', views.assoc_hat, name='assoc_hat'),
    path('penguins/<int:penguin_id>/unassoc_hat/<int:hat_id>/', views.unassoc_hat, name='unassoc_hat'),
    path('hats/', views.HatList.as_view(), name='hats_index'),
    path('hats/create/', views.HatCreate.as_view(), name='hats_create'),
    path('hats/<int:pk>', views.HatDetail.as_view(), name='hats_detail'),
    path('hats/<int:pk>/update/', views.HatUpdate.as_view(), name='hats_update'),
    path('hats/<int:pk>/delete/', views.HatDelete.as_view(), name='hats_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]