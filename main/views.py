from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from django.views import generic
from .models import navbar_up,navbar_basic,contact_us,slider_up,NewMain,footer_comment,PartsCommentCenter,service,serviceitem,about,NavbarUnder,comment_center,CommentCenterButton,AdMain
from django.utils import translation
from blog.models import Post, Comment
from news.models import New

# Create your views here.
class PageViewFull(TemplateView):
    template_name = "index.htm"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Post.objects.all().order_by("-created_on")[:6]
        context['header'] = navbar_up.objects.all()
        context['menu'] = navbar_basic.objects.all()
        #context['navbarunder'] = NavbarUnder.objects.select_related('navbar_basic__id','navar_id').all
        context['navbarunder'] = NavbarUnder.objects.all()
        #context['navbarunder'] = NavbarUnder.objects.filter(NavbarUnder_menu_link_u_contains=id).all()
        context['contact_us'] = contact_us.objects.all()
        context['slider_up'] = slider_up.objects.all()
        context['footer_comments'] = footer_comment.objects.all()
        context['PartsCommentCenter'] = PartsCommentCenter.objects.all().order_by('-id')[:3]
        context['commentcenterbutton'] = CommentCenterButton.objects.all().order_by('-id')[:1]
        context['admain'] = AdMain.objects.all().order_by('-id')[:10]
        context['comment_center'] = comment_center.objects.all()
        context['services'] = service.objects.all()
        context['serviceitems'] = serviceitem.objects.all()
        context['posts'] = Post.objects.all().order_by("-created_on")
        context['news'] = New.objects.all().order_by("-created_on")
        #context['about'] = About.objects.all()
        return context
        
# def news_detail(request, pk, template_name='new_detail.html'):
    # news= get_object_or_404(NewMain, pk=pk)    
    # return render(request, template_name, {'news':news})

def aboutus(request, template_name='about-us.htm'):  
    menu = navbar_basic.objects.all()  
    footer_comments = footer_comment.objects.all()
    contact_uss = contact_us.objects.all()
    abouts = about.objects.all()
    return render(request, template_name, {'about':abouts,'menu':menu,'footer_comments':footer_comments,'contact_us':contact_uss})
def contact(request, template_name='contact.html'):
    menu = navbar_basic.objects.all()  
    footer_comments = footer_comment.objects.all()
    services = service.objects.all()
    header = navbar_up.objects.all()
    contact_uss = contact_us.objects.all()
    contact = contact_us.objects.all()
    return render(request, template_name, {'contact':contact,'menu':menu,'footer_comments':footer_comments,'contact_us':contact_uss,'servicess':services,'headers':header})