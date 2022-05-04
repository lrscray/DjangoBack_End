from django.contrib import admin

# Register your models here.

#to use models in admin panel. register them
from .models import Note

admin.site.register(Note)