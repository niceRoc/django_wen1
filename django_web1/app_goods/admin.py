from django.contrib import admin
from models import GoodsInfo, GoodsType

# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'g_title']


admin.site.register(GoodsType, TypeAdmin)


class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'g_title', 'g_price', 'g_unit', 'g_stock', 'g_click']


admin.site.register(GoodsInfo, InfoAdmin)
