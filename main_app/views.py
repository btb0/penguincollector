from django.shortcuts import render

# Temporary Data until implementing models
penguins = [
    {'name': 'Nora', 'species': 'Adélie', 'description': 'cute and small', 'age': 3},
    {'name': 'Walter', 'species': 'Emperor', 'description': 'a little tubby but still cute', 'age': 4},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def penguins_index(request):
    return render(request, 'penguins/index.html', {
        'penguins': penguins
    })