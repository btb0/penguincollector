from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Penguin, Hat
from .forms import FeedingForm

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
    # instantiates FeedingForm to be rendered in the detail template
    feeding_form = FeedingForm()
    return render(request, 'penguins/detail.html', {
        'penguin': penguin,
        'feeding_form': feeding_form
    })

def add_feeding(request, penguin_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.penguin_id = penguin_id
        new_feeding.save()
    return redirect('penguins_detail', penguin_id=penguin_id)

# ====Class Based Views====

class PenguinCreate(CreateView):
    model = Penguin
    fields = '__all__'

class PenguinUpdate(UpdateView):
    model = Penguin
    # Not allowed to update the name
    fields = ['species', 'description', 'age']

class PenguinDelete(DeleteView):
    model = Penguin
    success_url = '/penguins'


# HATS CBVs
class HatList(ListView):
    model = Hat

class HatCreate(CreateView):
    model = Hat
    fields = '__all__'

class HatDetail(DetailView):
    model = Hat