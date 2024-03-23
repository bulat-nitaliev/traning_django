from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm



class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt','comment_text',)
    readonly_fields = ('comment_dt',)
    extra = 0


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id','order_dt','order_name','order_phone','order_status',)   
    list_display_links = ('id','order_name',)
    list_filter = ('order_status',)
    fields = ('order_dt','order_phone','order_status',)
    readonly_fields = ('order_dt',)
    search_fields = ('order_dt','order_phone','order_name',)
    list_editable = ('order_status',)
    list_per_page = 10
    list_max_show_all = 100
    inlines = [Comment,]
    
# Register your models here.
@admin.register(StatusCrm)
class StatusCrmModelAdmin(admin.ModelAdmin):
    list_display = ('status_name',)

@admin.register(CommentCrm)
class CommentCrmModelAdmin(admin.ModelAdmin):
    list_display = ('comment_binding','comment_text','comment_dt')
    fields = ('comment_binding','comment_text','comment_dt',)
    readonly_fields = ('comment_dt',)
