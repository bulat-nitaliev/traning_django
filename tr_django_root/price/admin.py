from django.contrib import admin
from price.models import PriceCard, PriceTable

@admin.register(PriceCard)
class PriceCardModelAdmin(admin.ModelAdmin):
    list_display = (
        'pc_value',
        'pc_description'
    )

@admin.register(PriceTable)
class PriceTableModelAdmin(admin.ModelAdmin):
    list_display = (
        'pt_title',
        'pt_old_price',
        'pt_new_price',
    )


# Register your models here.


