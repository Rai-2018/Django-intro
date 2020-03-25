from django.contrib import admin

# Register your models here.
#relative import, import Product class(defined in model) from models.py
from .models import Product

admin.site.register(Product)