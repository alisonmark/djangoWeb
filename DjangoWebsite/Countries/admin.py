from django.contrib import admin

# Register your models here.
from .models import countries, pop

admin.site.register(countries)
admin.site.register(pop)
