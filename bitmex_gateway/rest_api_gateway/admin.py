from django.contrib import admin

from .models import Account, Order

admin.register(Account, Order)(admin.ModelAdmin)
