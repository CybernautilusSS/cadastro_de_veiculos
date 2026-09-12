
from django.contrib import admin

from .models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'tipo',
        'marca',
        'modelo',
        'placa',
        'ano',
        'cor',
        'combustivel',
        'quilometragem',
        'data_cadastro',
    )

    list_filter = (
        'tipo',
        'combustivel',
        'ano',
    )

    search_fields = (
        'marca',
        'modelo',
        'placa',
    )

    ordering = (
        '-data_cadastro',
    )

