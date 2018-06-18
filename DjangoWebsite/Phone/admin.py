from django.contrib import admin

# Register your models here.
from .models import Category, iPhone, Sony

class IPhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'imodel')
    fields = ('name', 'imodel', 'category')
    list_filter = ('imodel',)
    search_fields = ('name',)


class SonyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sony_model')
    # fields = ('name', 'imodel', 'category')
    list_filter = ('sony_model',)
    search_fields = ('name',)


class IPhoneInline(admin.TabularInline):
    model = iPhone
    # min_num = 2
    # max_num = 5
    extra = 3
    list_display = ('name',)


class SonyInline(admin.TabularInline):
    model = Sony
    # min_num = 2
    # max_num = 5
    extra = 3
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pubDate')
    inlines = [IPhoneInline, SonyInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(iPhone, IPhoneAdmin)
admin.site.register(Sony, SonyAdmin)
