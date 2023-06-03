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
    # list of all hats penguin has
    id_list = penguin.hats.all().values_list('id')
    # Query for hats with an id not included in id_list (w/ exclude method)
    avail_hats = Hat.objects.exclude(id__in=id_list)
    # instantiates FeedingForm to be rendered in the detail template
    feeding_form = FeedingForm()
    return render(request, 'penguins/detail.html', {
        'penguin': penguin,
        'feeding_form': feeding_form,
        'hats': avail_hats
    })

def add_feeding(request, penguin_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.penguin_id = penguin_id
        new_feeding.save()
    return redirect('penguins_detail', penguin_id=penguin_id)

# ==== Penguin Class Based Views====

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

class HatUpdate(UpdateView):
    model = Hat
    fields = ['type', 'color']

class HatDelete(DeleteView):
    model = Hat
    success_url = '/hats'


def assoc_hat(request, penguin_id, hat_id):
    # Add hat to penguins collection
    Penguin.objects.get(id=penguin_id).hats.add(hat_id)
    return redirect('penguins_detail', penguin_id=penguin_id)


def unassoc_hat(request, penguin_id, hat_id):
    # remove hat from penguins collection
    Penguin.objects.get(id=penguin_id).hats.remove(hat_id)
    return redirect('penguins_detail', penguin_id=penguin_id)