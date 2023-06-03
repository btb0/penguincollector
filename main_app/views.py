from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required # Authorization for view functions
from django.contrib.auth.mixins import LoginRequiredMixin # Authorization for class based views
from .models import Penguin, Hat
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def penguins_index(request):
    # Retrieves ALL penguins
    # penguins = Penguin.objects.all()
    # Retrieves USER'S penguins
    penguins = Penguin.objects.filter(user=request.user)
    return render(request, 'penguins/index.html', {
        'penguins': penguins
    })

@login_required
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

@login_required
def add_feeding(request, penguin_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.penguin_id = penguin_id
        new_feeding.save()
    return redirect('penguins_detail', penguin_id=penguin_id)

# ==== Penguin Class Based Views====

class PenguinCreate(LoginRequiredMixin, CreateView):
    model = Penguin
    fields = ['name', 'species', 'description', 'age']

    # overriding inherited method (called when a valid penguin form is submitted)
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        # form.instance is the penguin.
        form.instance.user = self.request.user 
        return super().form_valid(form)

class PenguinUpdate(LoginRequiredMixin, UpdateView):
    model = Penguin
    # Not allowed to update the name
    fields = ['species', 'description', 'age']

class PenguinDelete(LoginRequiredMixin, DeleteView):
    model = Penguin
    success_url = '/penguins'


# HATS CBVs
class HatList(LoginRequiredMixin, ListView):
    model = Hat

class HatCreate(LoginRequiredMixin, CreateView):
    model = Hat
    fields = '__all__'

class HatDetail(LoginRequiredMixin, DetailView):
    model = Hat

class HatUpdate(LoginRequiredMixin, UpdateView):
    model = Hat
    fields = ['type', 'color']

class HatDelete(LoginRequiredMixin, DeleteView):
    model = Hat
    success_url = '/hats'

@login_required
def assoc_hat(request, penguin_id, hat_id):
    # Add hat to penguins collection
    Penguin.objects.get(id=penguin_id).hats.add(hat_id)
    return redirect('penguins_detail', penguin_id=penguin_id)

@login_required
def unassoc_hat(request, penguin_id, hat_id):
    # remove hat from penguins collection
    Penguin.objects.get(id=penguin_id).hats.remove(hat_id)
    return redirect('penguins_detail', penguin_id=penguin_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # creates a 'user' form object including data from browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save user to db
            user = form.save()
            # automatically login user after signup
            login(request, user)
            return redirect('penguins_index')
        else:
            error_message = 'Invalid sign up. Please try again.'
    # Either a GET request or bad POST request - render signup.html with empty form
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })