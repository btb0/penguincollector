from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Penguin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def penguins_index(request):
    penguins = Penguin.objects.all()
    return render(request, 'penguins/index.html', {
        'penguins': penguins
    })

def penguins_detail(request, penguin_id):
    penguin = Penguin.objects.get(id=penguin_id)
    return render(request, 'penguins/detail.html', {
        'penguin': penguin
    })

class PenguinCreate(CreateView):
    model = Penguin
    fields = '__all__'