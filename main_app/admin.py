from django.contrib import admin
from .models import Penguin, Feeding, Hat, Photo

# Register your models here.
admin.site.register(Penguin)
admin.site.register(Feeding)
admin.site.register(Hat)
admin.site.register(Photo)
