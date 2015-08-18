from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['flavor', 'price']
    list_display = ['flavor', 'ingredients']

admin.site.register(Pizza, PizzaAdmin)
