from django.contrib import messages,admin
from .models import navbar_up, navbar_basic, slider_up, contact_us, footer_comment,CategoryNew,NewMain,comment_center,PartsCommentCenter,service,serviceitem,about,NavbarUnder,CommentCenterButton,AdMain
from django.contrib.admin import AdminSite

class RemoveAdminDefaultMessageMixin:

    def remove_default_message(self, request):
        storage = messages.get_messages(request)
        try:
            del storage._queued_messages[-1]
        except KeyError:
            pass
        return True

    def response_add(self, request, obj, post_url_continue=None):
        """override"""
        response = super().response_add(request, obj, post_url_continue)
        self.remove_default_message(request)
        return response

    def response_change(self, request, obj):
        """override"""
        response = super().response_change(request, obj)
        self.remove_default_message(request)
        return response

    def response_delete(self, request, obj_display, obj_id):
        """override"""
        response = super().response_delete(request, obj_display, obj_id)
        self.remove_default_message(request)
        return response

# Register your models here.
# class HeaderAdmin(admin.ModelAdmin):
#     list_display = ('HeaderName', 'HeaderLink'),

# admin.site.register(navbar_up)
# admin.site.site_header = 'مدیریت سایت'
# admin.site.index_title = 'سایت بورس'             
#admin.site.site_title = 'HTML title from adminsitration'  
class SliderMainAdmin(RemoveAdminDefaultMessageMixin,admin.ModelAdmin):
    pass
    list_display = ('image',)
    list_display_links = ('image',)
    search_fields = ['image',]
    list_filter = ('image',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)
   
class NavbarBasicAdmin(RemoveAdminDefaultMessageMixin,admin.ModelAdmin):
    pass
    list_display = ('menu_name','menu_link',)
    list_display_links = ('menu_name','menu_link',)
    search_fields = ['menu_name','menu_link',]
    list_filter = ('menu_name','menu_link',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)
        
class FooteCommentAdmin(RemoveAdminDefaultMessageMixin,admin.ModelAdmin):
    pass
    list_display = ('title','description',)
    list_display_links = ('title','description',)
    search_fields = ['title','description',]
    list_filter = ('title','description',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)

class PartsCommentCenterAdmin(RemoveAdminDefaultMessageMixin,admin.ModelAdmin):
    pass
    list_display = ('service','description',)
    list_display_links = ('service','description',)
    search_fields = ['service','description',]
    list_filter = ('service','description',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)      
class ContactAdmin(RemoveAdminDefaultMessageMixin,admin.ModelAdmin):
    pass
    list_display = ('tell','email','adress',)
    list_display_links = ('tell','email','adress',)
    search_fields = ['tell','email','adress',]
    list_filter = ('tell','email','adress',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)
        
class NewAdmin(RemoveAdminDefaultMessageMixin,admin.ModelAdmin):
    pass
    list_display = ('title','body','created_on',)
    list_display_links = ('title','body',)
    search_fields = ['title','body',]
    list_filter = ('title','body','created_on',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)
        
class AdAdminMenuUnder(RemoveAdminDefaultMessageMixin,admin.ModelAdmin):
    pass
    list_display = ('menu_name_u','menu_link_u',)
    list_display_links = ('menu_name_u','menu_link_u',)
    search_fields = ['menu_name_u','menu_link_u',]
    list_filter = ('menu_name_u','menu_link_u',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)

class AdAdmin(RemoveAdminDefaultMessageMixin,admin.ModelAdmin):
    pass
    list_display = ('title','servicetopic','image',)
    list_display_links = ('title','servicetopic','image',)
    search_fields = ['title','servicetopic','image',]
    list_filter = ('title','servicetopic','image',)
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)
# class CategoryAdmin(admin.ModelAdmin):
    # pass
# admin.site.register(New, NewAdmin)
# admin.site.register(Category, CategoryAdmin)

class MessageAdmin(RemoveAdminDefaultMessageMixin, admin.ModelAdmin):
    pass
    def save_model(self, request, obj, form, change):
        self.message_user(request, 'با موفقیت ثبت شد.')
        return super().save_model(request, obj, form, change)
admin.site.site_header = 'مدیریت سایت'

admin.site.register(navbar_up, NavbarBasicAdmin)
admin.site.register(navbar_basic, NavbarBasicAdmin)
admin.site.register(slider_up, SliderMainAdmin)
admin.site.register(contact_us, ContactAdmin)
admin.site.register(comment_center, MessageAdmin)
admin.site.register(footer_comment, FooteCommentAdmin)
admin.site.register(service, MessageAdmin)
admin.site.register(about, MessageAdmin)
admin.site.register(NavbarUnder, AdAdminMenuUnder)
