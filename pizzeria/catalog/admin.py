from django.contrib import admin

from .models import Pizza, Zakaz, Seller, Terminal

admin.site.register(Pizza)
admin.site.register(Zakaz)
admin.site.register(Seller)
admin.site.register(Terminal)

