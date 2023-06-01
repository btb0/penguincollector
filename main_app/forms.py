from django.forms import ModelForm
from .models import Feeding

# Creating custom form for users to be able to add new feedings
# for penguins, displayed on the same detail.html page
class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal', 'food']