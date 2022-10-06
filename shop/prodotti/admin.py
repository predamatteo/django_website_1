from django.contrib import admin
from .models import Prodotto


class ProdottoAdmin(admin.ModelAdmin):
    list_display = (
        'nome','prezzo','scorta'
    )
admin.site.register(Prodotto, ProdottoAdmin)
