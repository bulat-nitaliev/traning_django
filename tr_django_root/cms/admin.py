from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe



@admin.register(CmsSlider)
class SliderModelAdmin(admin.ModelAdmin):
    list_display = ('cms_title','cms_text','cms_img','get_img',)
    fields = ('cms_title','cms_text','cms_img','get_img',) 
    list_display_links = ('cms_title',)
    readonly_fields = ('get_img',)

    def get_img(self,obj):
        return mark_safe(f'<img src="{ obj.cms_img.url}" width="80px"') if obj.cms_img else 'Нет картинки'
    
    get_img.short_description = 'Миниатюра'
    

    
