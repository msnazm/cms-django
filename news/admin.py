from django.contrib import admin
from news.models import New

class NewAdmin(admin.ModelAdmin):
    pass
    list_display = ('title','created_on',)
    list_display_links = ('title',)
    search_fields = ['title','body',]
    list_filter = ('title','created_on',)
    list_per_page = 2
    
admin.site.register(New, NewAdmin)
