from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    pass
    list_display = ('title','created_on',)
    list_display_links = ('title',)
    search_fields = ['title','body',]
    list_filter = ('title',)
    list_per_page = 10
    
admin.site.register(Post, PostAdmin)


# class BlogAdmin(admin.ModelAdmin):
    # list_display = ('title','created','updated',)
    # search_fields = ['title','body',]
    # list_filter = ('Date Created','Date Updated',)
    # inlines = [CommentInline,]